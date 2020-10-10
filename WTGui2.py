#attempt 2, have less opp and rather just straight access the sensors
import io 
import time
import VL53L1X
import keyboard
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_bus=0x29)
tank_depth = 0
minTemp = 0
maxTemp = 0
flag = True


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
    tank_depth = list_of_lines[0]
    minTemp = list_of_lines[1]
    maxTemp = list_of_lines[2]


def get_WaterLevel():
    global tank_depth
    distance_in_mm = tof.get_distance()
    wl = 1 - (distance_in_mm/1000)/tank_depth
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

def set_min_Temp(data):
    global minTemp
    minTemp = data
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[1] = str(tank_depth)

    a_file = open("config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()

def set_max_Temp(data):
    global maxTemp
    maxTemp = data
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    list_of_lines[2] = str(tank_depth)

    a_file = open("config.txt","w")
    a_file.writelines(list_of_lines)
    a_file.close()

def get_air_temp():
    airtemp = 30 # insert code to get air temperature
    return airtemp

def get_water_temp():
    watertemp = 20 # insert code to get water temperature
    return watertemp

def menu():
    global flag
    while flag:
	print("\nWelcome to Water Tank Managmnet")
	print("Please select a choice")
	print("1 to view data, 2 to set tank depth, 3 to set minimum Temperature , 4 to set maximum Temperature,5 to monitor, 6 to quit")
	choice = input("Enter a command:\n")
	if choice == 1:
			#get all data, airTemperature and waterTemperature , water level
			#airTemperature = 
			#waterTemperature = 
            wlevel = get_WaterLevel()
            print("the water level is: "+str(wlevel)+"%")
			
	elif choice == 2:
			#set Matts max water depth
			wlMax= input("enter depth in m\n")
			wlMax = float(wlMax)
			set_tank_depth(wlMax)
			print("Tank depth has been updated to to: "+str(wlMax)+"m")

    elif choice == 3:
			#set minimum temperature warning flag
			tmin= input("enter minimum temperatue in celsius\n")
			tmin = float(tmin)
			set_min_Temp(tmin)
			print("Tank depth has been updated to to: "+str(tmin)+")

    elif choice == 4:
			#set maximum temperature warning flag
			tmax= input("enter maximum temperatue in celsius\n")
			tmax = float(tmax)
			set_max_Temp(tmax)
			print("Tank depth has been updated to to: "+str(tmax)+")

    elif choice == 5:
        print("press the w key to wake up")
        monitor()
        flag = False

	elif choice == 6:
			flag = False
			print("goodbye")
	else:
		print("invalid input, please try again")

def monitor():
    #do stuff in background
    global flag
    if keyboard.is_pressed("w"):
        flag = True
        menu()
    else:
        if(get_air_temp() > maxTemp):
            print("Warning air temperature has exceeded maximum temperate allowed")
        elif( get_air_temp() < minTemp):
            print("Warning air temperature has exceeded minimum temperate allowed")
        if(get_water_temp() > maxTemp):
            print("Warning water temperature has exceeded maximum temperate allowed")
        elif( get_water_temp() < minTemp):
            print("Warning water temperature has exceeded minimum temperate allowed")  
        else:
            #monitor water level in background. collect data
            

    
