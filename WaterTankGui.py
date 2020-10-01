#made my Matthew
#basic GUI/input for API

import Waterlevel
import Temperature
flag = True


while flag:
	print("\nWelcome to Water Tank Managmnet")
	print("Please select a choice")
	print("1 to view temperature data, 2 to view waterlevel data, 3 to set tank depth, 4 to quit")
	
	choice = input("Enter a command:\n")
	if choice == 1:
			#get Rosses data, airTemperature and waterTemperature
			airTemperature = Temperature.GetWaterTemp()
			waterTemperature = Temperature.GetOutSideTemp()
			print("The air temperature is: "+str(airTemperature)+"\nThe water Temperature is: "+str(waterTemperature))
	elif choice == 2:
			#get Matt Data, water level
			waterper = Waterlevel.getPercentFull()
			print("the water level is: "+str(waterper)+"%")
	elif choice == 3:
			#set Matts max water depth
			wlMax= input("enter depth in m\n")
			wlMax = float(wlMax)
			Waterlevel.setMax(wlMax)
			print("Tank depth set to: "+str(Waterlevel.getMax())+"m")
	elif choice == 4:
			flag = False
			print("goodbye")
	else:
		print("invalid input, please try again")
