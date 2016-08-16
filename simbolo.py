class Simbolo:
	def __init__(self, totalSimb, totalLido):
		self.__freq = float(totalSimb) / float(totalLido)
		#self.__byteArray = [];
		#TODO: See what this class needs to have.
	
	def getFreq(self):
		return self.__freq
