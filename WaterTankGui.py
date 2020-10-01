#made my Matthew
#basic GUI/input for API

flag = true

while flag:
	print("Welcome to Water Tank Managmnet")
	print("Please select a choice")
	print("1 to view temperature data, 2 to view waterlevel data, 3 to set tank depth, 4 to quit")
	
	choice = input("Enter a command:\n")
	if choice = 1:
			#get Rosses data, airTemperature and waterTemperature
			airTemperature = Tempsensors.getAirTemp()
			waterTemperature = Tempsensor.getWaterTemp()
			print("The air temperature is: "+str(airTemperature)+"\nThe water Temperature is: "+str(waterTemperature)
	elif choice=2:
			#get Matt Data, water level
			water = waterLevel.getWaterLevel() 
			print("the water level is: +str(waterLevel)
	elif choice=3:
			#set Matts max water depth
			wlMax= input("enter depth in m")
			waterLevel.setMaxdepth(wlMax)
			println("Tank depth set to: "+str(wlMax)
	elif choice=4:
			flag = false
			print("goodbye"
	else:
		print("invalid input, please try again")
