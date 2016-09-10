import simbolo
import sys
"""
TODO:  Cant find a way to simply write a byte
	   Maybe we'll have to use some python
	   functionality, like Struct or BytesIO
	   (Still havent looked ate it though)

	   This is proving to be more tricky than
	   what we've thought it would be.
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
	
	temp = buff.BYTE_SIZE - 1

	for bit in simb.getCode():
		if buff.length == buff.BYTE_SIZE:
			byte = chr(buff.buffr) #bytes(buff.buffr)
			fOut.write(byte)
			buff.length = buff.buffr = 0
	
		if bit == '1':
			buff.buffr |= (1 << (temp - buff.length))
	#	else:
	#		buff.buffr &= ~(1 << (temp - buff.length))
		buff.length += 1

# http://stackoverflow.com/questions/16022556/has-python-3-2-to-bytes-been-back-ported-to-python-2-7
def to_bytes(n, length, endianess='big'):
	h = '%x' % n
	s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
	return s if endianess == 'big' else s[::-1]
