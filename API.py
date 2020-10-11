#attempt 2, have less opp and rather just straight access the sensors
import io 
import time
import VL53L1X
import keyboard

tank_depth = 0
minTemp = 0
maxTemp = 0
flag = True
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)

def setup():
    global tof    
    global tank_depth
    global minTemp
    global maxTemp
    # starting tof sensor in Long range witch is up to 4m
    tof.open()
    tof.start_ranging(3)

    #Ross please put your setup here
    #bla bla

    #config values, taken from a config file
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines = list_of_lines
    tank_depth = list_of_lines[0]#.rstrip()
    minTemp = list_of_lines[1]
    maxTemp = list_of_lines[2]
    a_file.close()
    pass

def get_config():
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    a_file.close()
    return list_of_lines

def get_WaterLevel():
    global tank_depth
    global tof
    distance_in_mm = int(tof.get_distance())
    print(distance_in_mm)
    wl = float( 1 - (distance_in_mm/1000.0)/float(tank_depth))*100.0
    return wl


def set_tank_depth(data):
    global tank_depth
    tank_depth = data
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[0] = str(tank_depth)

    a_file = open("config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()
    pass

def set_min_Temp(data):
    global minTemp
    minTemp = data
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[1] = str(tank_depth)

    a_file = open("config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()
    pass

def set_max_Temp(data):
    global maxTemp
    maxTemp = data
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[2] = str(tank_depth)

    a_file = open("config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()
    pass

def get_air_temp():
    airtemp = 30 # insert code to get air temperature
    return airtemp

def get_water_temp():
    watertemp = 20 # insert code to get water temperature
    return watertemp

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
		    print("the minimum temperature has been updated to to: "+str(tmin)+"m")
        elif (choice == 4):
		    #set maximum temperature warning flag
		    tmax= input("enter maximum temperatue in celsius\n")
		    tmax = float(tmax)
		    set_max_Temp(tmax)
		    print("the minimum temperature has been updated to to: "+str(tmax)+"m")
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
    warningflag = False
    if keyboard.is_pressed("w"):
        flag = True
        menu()
    else:
        if(get_air_temp() > maxTemp):
            print("Warning air temperature has exceeded maximum temperate allowed!!")
            warningflag = True

        if( get_air_temp() < minTemp):
            print("Warning air temperature has exceeded minimum temperate allowed")
            warningflag = True

        if(get_water_temp() > maxTemp):
            print("Warning water temperature has exceeded maximum temperate allowed")
            warningflag = True

        if( get_water_temp() < minTemp):
            print("Warning water temperature has exceeded minimum temperate allowed")
            warningflag = True

        if(get_WaterLevel() < 50):
            print("Tank is 5% or less full, please disconnect from rainwater tank and swop to mains water")
            warningflag = True

        else:
            #monitor water level in background. collect data




            if(warningflag):
                print("please fix issue then relaunch app")
                exit()
    pass

# Main that is executed when program starts
if __name__ == "__main__":
    try:
        # Call setup function
        setup()
        menu()
    except Exception as e:
        print(e)


          

    
