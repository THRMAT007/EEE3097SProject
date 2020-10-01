#Crated by Matthew Thorburn
#EEE3097S porject
#class to handle the Water level measurments for the API


wMax = 1.0
wlevel = 0.0

def getPercentFull():
	clevel = getWaterLevel()
	#print(str(clevel))
	cmax = getMax()
	#print(str(cmax))
	return(clevel/cmax * 100)

def setMax(num):
	wMax=num
	print(str(wMax))

def getMax():
	return(wMax)

def getWaterLevel():
	wlevel  = 523.1/1000 # get sensor data
	return(wlevel)
