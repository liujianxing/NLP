import pickle
import sys

#defaults 
inputfile = "input.txt"
outputfile = "input.pkl"
dictionary = "dict.pkl"

if len(sys.argv) > 0:
	inputfile = sys.argv[1]
	outputfile = sys.argv[2]
	dictionary = sys.argv[3]

fin = open(inputfile,"r")

dic = {}
spk_dic = {}

out = []
spk_out = [] 

code = 0
speaker = 0
for line in fin:
	lout = []
	spk = line[0]
	s = speaker
	if spk in spk_dic:
		s = spk_dic[spk]
	else:
		spk_dic[spk] = speaker
		speaker += 1	

	for w in line.split()[1:]:
		c = code
		if w in dic:
			c = dic[w]
		else:
			dic[w] = code
			code +=1
		lout.append(c)

	out.append(lout)
	spk_out.append(s)

pickle.dump([out,spk_out], open(outputfile,"w"))
pickle.dump([spk_dic, dic], open(dictionary,"w"))

fin.close()
