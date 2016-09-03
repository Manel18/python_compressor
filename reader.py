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
