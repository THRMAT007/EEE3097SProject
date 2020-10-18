#attempt 2, have less opp and rather just straight access the sensors
import io 
import os
import time
import VL53L1X
import keyboard
import datetime
from datetime import timedelta
import time
import sqlite3
from sqlite3 import Error

conn =None
tank_depth = None
minTemp = None
maxTemp = None
flag = True
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)

def setup():
    global tof    
    global tank_depth
    global minTemp
    global maxTemp
    # starting tof sensor in Long range which is up to 4m
    tof.open()
    tof.start_ranging(3)

    #Ross please put your setup here
    #bla bla

    # database setup
    create_connection(r"./Data/pythonsqlite.db")
    insert_table(r"./Data/pythonsqlite.db",('12/10/2020','32','45','45','12'))
    print(read_table(r"./Data/pythonsqlite.db"))
    #config values, taken from a config file
    a_file = open("./Data/config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines = list_of_lines
    tank_depth = float(list_of_lines[0].rstrip())
    minTemp = float(list_of_lines[1].rstrip())
    maxTemp = float(list_of_lines[2])
    a_file.close()
    pass

def get_config():
    a_file = open("./Data/config.txt","r")
    list_of_lines = a_file.readlines()
    a_file.close()
    return list_of_lines

def get_WaterLevel():
    global tank_depth
    global tof
    distance_in_mm = int(tof.get_distance())
    wl = float( 1 - (distance_in_mm/1000.0)/float(tank_depth))*100.0
    wl = round(wl,1)
    return wl


def set_tank_depth(data):
    global tank_depth
    tank_depth = float(data)
    a_file = open("./Data/config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[0] = str(tank_depth)+"\n"

    #print (list_of_lines)
    a_file = open("./Data/config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()
    pass

def set_min_Temp(data):
    global minTemp
    minTemp = float(data)
    a_file = open("./Data/config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[1] = str(minTemp)+"\n"

    a_file = open("./Data/config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()
    pass

def set_max_Temp(data):
    global maxTemp
    maxTemp = float(data)
    a_file = open("./Data/config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[2] = str(maxTemp)

    a_file = open("./Data/config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()
    pass

def get_air_temp():
    airtemp = 30 # insert code to get air temperature
    return airtemp

def get_water_temp():
    watertemp = 20 # insert code to get water temperature
    return watertemp

def create_connection(db_file):
    #creats a database coonnection to a sqlite database
    global conn
    try:
        conn = sqlite3.connect(db_file)
        #print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def insert_table(db_file,mydata):
    #create a new project into the project table
    connect = sqlite3.connect(db_file)
    cur = connect.cursor()
    #Assuming table has already been created
    #cur.execute('CREATE TABLE waterlevel (date VARCHAR, midnight VARCHAR, morning VARCHAR, noon VARCHAR, evening VARCHAR)')
    #connect.commit()
    sqlite_insert = '''INSERT INTO waterlevel (date, midnight, morning, noon, evening) values (?, ?,?,?,?)'''
    cur.execute(sqlite_insert,mydata)
    #cur.execute('INSERT INTO waterlevel (date, midnight, morning, noon, evening) values ("18/10/2020", "75","64","59","23")')
    connect.commit()
    connect.close()
    


def read_table(db_file):

    connect = sqlite3.connect(db_file)
    cur = connect.cursor()
    cur.execute('SELECT * FROM waterlevel ORDER BY date ASC')
    data_1 = cur.fetchall()

    connect.close()
    return data_1


def menu():
    global flag
    global tank_depth
    global minTemp
    global tof
    global maxTemp
    while flag:
        print("\nWelcome to Water Tank Managmnet")
        print("Please select a choice")
        print("1 to view data, 2 to set tank depth, 3 to set minimum Temperature , 4 to set maximum Temperature,5 to monitor, 6 to quit")
        choice = input("Enter a command:\n")

        if choice==1:   
            con = get_config()
            print("config setting are")
            print("the tank depth is set at "+str(con[0])+"m . The minimum Temperature is: "+str(con[1])+" and the maximum Temperature is: "+str(con[2]))
            wlevel = get_WaterLevel()
            print("the water level is: "+str(wlevel)+"%")
            
        elif (choice == 2):
		    #set Matts max water depth
		    wlMax= input("enter depth in m\n")
		    wlMax = float(wlMax)
		    set_tank_depth(wlMax)
		    print("Tank depth has been updated to to: "+str(wlMax)+"m")
        elif (choice == 3):
		    #set minimum temperature warning flag
		    tmin= input("enter minimum temperatue in celsius\n")
		    tmin = float(tmin)
		    set_min_Temp(tmin)
		    print("the minimum temperature has been updated to to: "+str(tmin))
        elif (choice == 4):
		    #set maximum temperature warning flag
		    tmax= input("enter maximum temperatue in celsius\n")
		    tmax = float(tmax)
		    set_max_Temp(tmax)
		    print("the minimum temperature has been updated to to: "+str(tmax))
        elif (choice == 5):
            print("press the w key to wake up")
            monitor()
            flag = False
        elif (choice == 6):
            flag = False
            tof.stop_ranging()
            print("goodbye")
        else:
            print("invalid input, please try again")
    pass
		

def monitor():
    #do stuff in background
    global flag
    global minTemp
    global maxTemp
    Loading = ['\\____','/\___','_/\__','__/\_','___/\\','____/','_____']
    counter =0

    warningflag = False
    fl =True

    measuring = [True,True,True,True]
    lvlResults = ['55','34','11','39']
    dataStorage = datetime.date.today()

    print("press CTRL+C to exit idle")
    print("idling")
    starttime = time.time()
    
    while fl:      
        try:
            time.sleep(2)
            now = datetime.datetime.now()
            if now.hour == 0 and now.minute == 0 and measuring[0]:
                #print("it is time")
                measuring[0] = False

            if now.hour == 6 and now.minute == 0 and measuring[1]:
                #print("it is time")
                measuring[1] = False
            
            if now.hour == 12 and now.minute == 0 and measuring[2]:
                #print("it is time")
                measuring[2] = False
            
            if now.hour == 18 and now.minute == 0 and measuring[3]:
                #print("it is time")
                measuring[3] = False
            
            if(get_air_temp() > maxTemp):
                print("Warning air temperature has exceeded maximum temperate allowed!!")
                warningflag = True

            elif(get_air_temp() < minTemp):    
                print("Warning air temperature has exceeded minimum temperate allowed")
                warningflag = True

            elif(get_water_temp() > maxTemp):
                print("Warning water temperature has exceeded maximum temperate allowed")
                warningflag = True

            elif( get_water_temp() < minTemp):
                print("Warning water temperature has exceeded minimum temperate allowed")
                warningflag = True

            elif(get_WaterLevel() < 5):
                print("Tank is 5% or less full, please disconnect from rainwater tank and swop to mains water")
                warningflag = True
            
            if(warningflag):
                #print("please fix issue then relaunch app")
                fl = False
            else:
                #background recording of data
                if counter ==7:
                    counter=0              
                print(chr(27) + "[2J") # clears terminal
                print(Loading[counter])
                counter+=1

        except KeyboardInterrupt:
            print("exiting")
            fl=False
                
    print("done")
    print(measuring)
    j=0
    for x in measuring:
        if not x:
            j+=1
    
    storedata = ['']
    if(j>0):
        storedata[0]=dataStorage.strftime('%Y/%m/%d')
        k = 0
        for i in range(0,4):
            if not measuring[i]:
                storedata.append(lvlResults[i])
        print(storedata)          
        f=open("./Data/data.txt",'a+')
        for x in storedata:
            f.write(x+'\r\n')
        f.close()
    else:
        print("no data to store")

    print("\nwaking up")
    endtime = time.time() - starttime
    endtime = round(endtime)
    print("idled for: "+str(timedelta(seconds=endtime)))
    flag=True
    menu()
    pass

# Main that is executed when program starts
if __name__ == "__main__":
    try:
        # Call setup function
        setup()
        menu()
        
    except Exception as e:
        print(e)


          

    
