# EEE3097S Project
# by Matt and Ross
this repo contains the relevant file for out EEE3097S design project.
the APIWaterTank_3.py file is the final product, written in python 3.
the APIWaterTank_2.py file is written in python 2.7 and was discaded due to libaries for out senson only being availble of python3.

for the api to run the user needs to have enabled the i2c and spi interface on thier pi.
the api can be run using "python3 APIWaterTank_3.py" .  
  
    
to run the API:  
you need to pip3 install VL53L1X libary and pip3 install adafruit-circuitpython-mcp3xxx.  
you need the APIWaterTank_3.py file
in the same director as the APIWaterTank_3.py file you need a directory Data. in the Data direcotry the user needs to create a config.txt file. in the file the first line in the tank depth, second line is minimum temperature and the third line is the maximum temperature. on the users first time using they API they should uncomment line 46 , inseet_data_data() , so create the sqlite database. then close the API, and comment out line 46, and relaunch the API. Now the API shoudl be fully functional.
