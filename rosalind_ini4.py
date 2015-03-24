fr = open("rosalind_ini4.txt",'r')
fw = open("rosalind_ini4.res.txt",'w')
inputs = fr.read()

num = inputs.split()
num = map(int, num)

a = num[0]
b = num[1]

fw.write(str(sum(range(a|1, b+1, 2))))

fr.close()
fw.close()