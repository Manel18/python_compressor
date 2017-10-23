"""
TODO: - Remember to check out the toString method
	  - If the objects of this class wont have the 
	  	symbol they represent maybe we should change the name
		We'll see how it goes.
"""
class Simbolo:
	def __init__(self, simb, totalSimb, totalLido):
		self.__simb = simb
		self.__freq = float(totalSimb) / float(totalLido)
		self.__code = ""
		# The object will contain a string of 1's and 0's 
		# representing the shannon-fano encoding of it, 
		# we'll then use this in the write section to push
		# into the buffer this code (not the char '1' or '0')
		# if code == "0011" and the current state of the buffer
		# is 10110000 (assuming the buffer is a byte) then
		# we would have to make those last 4 bits 0011
		# Thats basically it :P

####### for sorting symbols by frequency #######
	def __lt__(self, other):
		return self.__freq < other.getFreq()

	def __eq__(self, other):
		return self.__freq == other.getFreq()
	
	def __gt__(self, other):
		return other.__lt__(self)
	
	def __ne__(self, other):
		return not self.__eq__(other)
################################################

	def getFreq(self):
		return self.__freq
	
	def getCode(self):
		return self.__code
	
	def getSimb(self):
		return self.__simb
	
	def appendBit(self, bit):
		self.__code += bit
