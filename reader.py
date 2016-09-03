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
	return count
