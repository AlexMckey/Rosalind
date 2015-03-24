f = open('rosalind_ini5.res.txt','w')
with open('rosalind_ini5.txt','r') as fr:
	f.write(''.join(fr.readlines()[1::2]))
f.close()