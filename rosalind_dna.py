fr = open("rosalind_dna.txt",'r')
fw = open("rosalind_dna.res.txt",'w')
#fr = open("rosalind_str1.sample.txt",'r')
#fw = open("rosalind_str1.sample.res.txt",'w')

st = fr.read().strip()

# очень короткое но емкое решение
#from collections import Counter
#for k,v in sorted(Counter(s).items()): print v,

s = set(st)
dict = {}
for i in s:
    dict[i] = 0
for i in st:
    dict[i] = dict[i] + 1
for key in sorted(dict):
    fw.write(str(dict[key]) + ' ')
    print key, dict[key]

fr.close()
fw.close()