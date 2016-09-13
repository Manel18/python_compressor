import simbolo
import sys

"""
TODO: We still have to write the table
	  We haveo to write at least 4 things for each symbol:
	  
	  1: The size of the table
		*the for each symbol*
	  2: The (byte-sized) symbol it self
	  3: The length of the shannon code for this symbol
	  4: The shannon fano code for the symbol
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
	num_bytes = 0
	# Write table here
	writeTable(simbs, fOut)
	# Write compressed file here
	fIn.seek(0,0)
	num_bytes += writeCompr(simbs,buff, fIn, fOut)
	return num_bytes;

def writeTable(simbs, fOut):
	byte_wrt = 0
	#write size of table
	size = len(simbs)
	fOut.write(chr(size))
	for i in simbs.keys():
		codeLen = len(simbs[i].getCode());
		fOut.write("{0}{1}{2}".format(i, chr(codeLen), simbs[i].getCode()))
		byte_wrt += (codeLen+2)
	
	return byte_wrt


def writeCompr(simbs, buff, fIn, fOut):
	byte_count = 0
	for i in fIn:
		for j in i:
			byte_count += writeToBinBuffer(buff, simbs[j], fOut)
	return byte_count

def writeToBinBuffer(buff, simb, fOut):
	
	temp = buff.BYTE_SIZE - 1
	byte_wrt = 0

	for bit in simb.getCode():
		if buff.length == buff.BYTE_SIZE:
			byte = chr(buff.buffr) #bytes(buff.buffr)
			fOut.write(byte)
			byte_wrt += 1
			buff.length = buff.buffr = 0
	
		if bit == '1':
			buff.buffr |= (1 << (temp - buff.length))
	#	I think we actually dont need the else statement
	#	else:
	#		buff.buffr &= ~(1 << (temp - buff.length))
		buff.length += 1
	return byte_wrt

# http://stackoverflow.com/questions/16022556/has-python-3-2-to-bytes-been-back-ported-to-python-2-7
def to_bytes(n, length, endianess='big'):
	h = '%x' % n
	s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
	return s if endianess == 'big' else s[::-1]
