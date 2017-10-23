import simbolo

def shannon(simbs, inf, sup):
	
	if inf == sup:
		return
	
	if sup-inf == 1:
		simbs[inf].appendBit('0')
		simbs[sup].appendBit('1')
	else:
		half = 0.0
		for x in range(inf,sup+1):
			half += simbs[x].getFreq()

		half *= 0.5

		counter = 0.0
		sepIndex = -1 # Separation index

		for x in range(inf, sup+1):
			if counter < half:
				simbs[x].appendBit('0')
				counter += simbs[x].getFreq()
			else:
				if sepIndex < 0:
					sepIndex = x
				simbs[x].appendBit('1')

		if sepIndex < 0:
			sepIndex = inf + 1

		shannon(simbs, inf, sepIndex-1)
		shannon(simbs, sepIndex, sup)
