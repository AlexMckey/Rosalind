fr = open("rosalind_rna.txt",'r')
fw = open("rosalind_rna.res.txt",'w')
#fr = open("rosalind_rna.sample.txt",'r')
#fw = open("rosalind_rna.sample.res.txt",'w')

st = fr.read().strip()
#st = 'AAAACCCGGT'

sr = st[::-1]
fw.write(sr)
print st
print sr

fr.close()
fw.close()