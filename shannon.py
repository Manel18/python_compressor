import simbolo

def shannon(simbs, inf, sup):
	if(inf > sup or inf < 0 or sup < 0 or sup > len(simbs)):
		raise SystemExit("Error!")
	
	if inf == sup:
		return
	
	if sup-inf == 1:
		simbs[inf].appendBit('0')
		simbs[sup].appendBit('1')
	else:
		half = 0.0
		for s in simbs[inf:sup+1]:
			half += s.getFreq()

		half *= 0.5

		counter = 0.0
		sepIndex = -1 # Separation index

		for x in range(inf, sup+1):
			counter += simbs[x].getFreq()
			if counter <= half:
				simbs[x].appendBit('0')
			else:
				if sepIndex < 0:
					diff1 = abs((counter-simbs[x].getFreq()) - half)
					diff2 = abs(counter - half)
					if diff1 <= diff2:
						sepIndex = x
						simbs[x].appendBit('1')
					else:
						sepIndex = x+1
						simbs[x].appendBit('0')
				else:
					simbs[x].appendBit('1')
		
		'''
		if sepIndex < 0:
			sepIndex = inf + 1
		'''
		shannon(simbs, inf, sepIndex-1)
		shannon(simbs, sepIndex, sup)
