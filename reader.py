import pickle
"""
TODO: - Find a better way to read the file, we cant read it line 
		by line (although the docs say its memory efficient and fast 
		https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files).
		It was for testing anyway. But it only works for text files
		so we're going to have to change this.
		Maybe find a good byte size and just f.read(size)
"""

def read_file( fich, simbs ):
	count = 0
	for i in fich:			# Reads line by line (?)
		for j in i:			# Reads char by char (?)
			count += 1
			if j in simbs:
				simbs[j] += 1
			else:
				simbs[j] = 1

	# Assuming the file was opened with vim
	# https://stackoverflow.com/a/31426524/5224705
	simbs['\n'] -= 1
	if simbs['\n'] == 0:
		del simbs['\n']
	return count-1

def binary(c):
	return '{0:08b}'.format(ord(c),'b')

# this is very inefficient right now
# just wanted to check if I was compressing 
# things successfully
# this will definitely be optimized!!
def unpack(f, fOut):
	simbs = pickle.load(f)
	simbs = dict((v,k) for k,v in simbs.iteritems())
	buffSize = max([len(k) for k in simbs.keys()])
	buff = ''
	c = ''
	while True:
		ch = f.read(1)
		if not ch: break
		buff += binary(ch);
	
	for b in buff:
		c += b
		if c in simbs:
			fOut.write(simbs[c])
			c = ''
	#print c
