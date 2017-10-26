import math

# Calculate information (bits)
def information(simb):
#	return math.log( (1 / simb.getFreq()), 2)
	return -math.log( simb.getFreq(), 2)

def entropy(simbs):
	total = 0.0
	for s in simbs:
		total += s.getFreq() * information(s)
	return total

def entropyLimit(n):
	return math.log(n, 2)
