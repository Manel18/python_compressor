import math

# Calculate information 
def information(simb):
	return math.log( (1 / simb.getFreq()), 2)

def entropy(simbs):
	total = 0.0
	for s in simbs:
		total += information(s) * s.getFreq()
	return total

def entropyLimit(n):
	return math.log(n, 2)
