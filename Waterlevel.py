#Crated by Matthew Thorburn
#EEE3097S porject
#class to handle the Water level measurments for the API
class Waterlevel():

	def __init__(self,num):
		self.wMax = num

	def getPercentFull(self):
		clevel = self.getWaterLevel()
		#print(str(clevel))
		cmax = self.getMax()
		#print(str(cmax))
		return(clevel/cmax * 100)

	def setMax(self,num):
		self.wMax=num

	def getMax(self):
		return(self.wMax)

	def getWaterLevel(self):
		wlevel  = 523.1/1000 # get sensor data
		return(wlevel)
