#attempt 2, have less opp and rather just straight access the sensors
import io 
import time
import VL53L1X
tof = VL53L1X.VL53L1X(i2c_bus=1, i2c_bus=0x29)
tank_depth = 0
minTemp = 0
maxTemp = 0



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

    #config values
    a_file = open("config.txt","r")
    list_of_lines = a_file.readlines()
    tank_depth = list_of_lines[0]
    minTemp = list_of_lines[1]
    maxTemp = list_of_lines[2]


def get_WaterLevel():
    distance_in_mm = tof.get_distance()
    return distance_in_mm

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
