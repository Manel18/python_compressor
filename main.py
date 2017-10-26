import os.path
import argparse
import simbolo
import reader
import utils
import shannon
import writer
import math
import sys

"""
TODO:
[x]	Reading the command line arguments works but we should
	probably make the messages more readable(?), a bit more
	nice to the eye :P

[x]	1- Check if files exist
[x]	2- Read and create dictionary ( { simb: total vezes que aparece no ficheiro } )
[x]	3 - Transform that into {simb: Simbolo}
[x]	4 - Do calculations, entropy and shit (see if file is worth compressing)
[x]	5 - Shannon fano
[x]	7 - write, byte per byte

	that's all folks :P
"""

parser = argparse.ArgumentParser("Compress some files")

# "nargs=+" -> gathers all the file names passed as arguments, in a list
parser.add_argument('files', nargs='+')

# debug flag
parser.add_argument('-d', action='store_true')

parser.add_argument('-check', action='store_true')

parser.add_argument('-u', action='store_true')

args = parser.parse_args()

if args.u:
	if len(args.files) == 2:
		fIn = open(args.files[0], 'r')
		fOut = open(args.files[1], 'w')
		reader.unpack(fIn,fOut)
		fIn.close()
		fOut.close()
		sys.exit(0)
	else:
		raise SystemExit("Finished")

real_files = []
for i in args.files:
	if not os.path.isfile(i):
		print "{0} does not exist!".format(i)
	else:
		real_files.append(i)

if len(real_files)==0:
	raise SystemExit("You entered no existing files!\nTerminating...")

simbolos = {} # simbolos -> { char x: how many x's are in the file }
for i in real_files:
	f = open(i, 'r')
	total_lido = reader.read_file(f, simbolos) # reads file, updates simbolos, returns number of bytes read
	
	# Transform simbolos -> { char x: Simbolo(#x's, total_lido) }
	for key in simbolos.keys():				   
		total_simb = simbolos[key]
		simbolos[key] = simbolo.Simbolo(key, total_simb, total_lido)
	
	# Sort by freq
	sortedList = sorted(simbolos.values(), reverse=True)
	
	'''
	for simb in sortedList:
		print "%s | %s" % (simb.toString(), utils.information(simb))
	'''

	# Entropy and shit -> decisions
	e = utils.entropy(sortedList)
	el = utils.entropyLimit(len(sortedList))
	if args.d: 
		print "Number of symbols: "+str(len(sortedList))
		print "Entropy: "+str(e)
		print "Entropy Limit: "+str(el)
		if e < 0 or e > el:
			raise SystemExit("Error: Entropy is out of of bounds!")
	
	if args.check:
		raise SystemExit("Entropy checked!")
	# Shannon
	shannon.shannon(sortedList, 0, len(sortedList)-1)
	
	if args.d:	
		total = 0.0
		Kr = 0.0
		H = 0.0
		for simb in sortedList:
			print "%s\t%f %d %f" % (simb.toString(), -math.log(simb.getFreq(), 2),len(simb.getCode()) ,-math.log(simb.getFreq(), 2)+1)
			#print "%s | %s" % (simb.toString(), utils.information(simb))
			total += simb.getFreq() * len(simb.getCode())
			Kr += 2**(-len(simb.getCode()))
		print "mean N: %f" % (total)
		print "Kr: %f" % (Kr)
		print "p: %f" % (e / total)
		print "c: %f" % ((math.log(len(sortedList),2)-total)/math.log(len(sortedList),2))
	
	#Assuming the model: <file_name>.<extension> 
	temp = i.split('.')
	newFileName = temp[0]+"_pack"	
	outFile = open(newFileName, "w")
	
	#write
	bytes_after_compress = 0
	teste = {}
	for i in sortedList:
		teste[i.getSimb()] = i.getCode()
	
	bytes_after_compress = writer.write(teste, f, outFile)
	
	'''	
	if args.d :
		print "Compression ratio: {0}".format((math.log(len(sortedList),2) - float(total/len(sortedList)))/float(math.log(len(sortedList),2)))
		#print "Compression ratio: {0}".format(float(total_lido)/float(bytes_after_compress));
	'''
	f.close()
	outFile.close();
