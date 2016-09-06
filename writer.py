import simbolo
import sys

"""
TODO:  Cant find a way to simply write a byte
	   Maybe we'll have to use some python
	   functionality, like Struct or BytesIO
	   (Still havent looked ate it though)
"""
##################################################

class BinBuffer:
	BYTE_SIZE = 8
	# ...
	# We can add all kinds of sizes
	# ...	
	def __init__(self, length):
		self.length = length
		self.buffr = 0

##################################################

def write(simbs, fIn, fOut):
	buff = BinBuffer(0)
	# Write table here
	# Write compressed file here
	fIn.seek(0,0)
	writeCompr(simbs,buff, fIn, fOut)

"""
def writeTable(simbs,buff, fOut):
	#Write Table
"""

def writeCompr(simbs,buff, fIn, fOut):
	for i in fIn:
		for j in i:
			writeToBinBuffer(buff, simbs[j], fOut)

def writeToBinBuffer(buff, simb, fOut):
	
	for bit in simb.getCode():
		if buff.length == buff.BYTE_SIZE:
			byte = bytes(buff.buffr)
			fOut.write(byte)
			buff.length = buff.buffr = 0

		if bit == '1':
			buff.buffr |= (1 << buff.length)
		else:
			buff.buffr &= ~(1 << buff.length)

		buff.length += 1
	
