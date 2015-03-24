fr = open('rosalind_ini3.txt', 'r')
fw = open('rosalind_ini3.res.txt', 'w')
a = fr.readlines()
s = a[0].strip()
t = a[1].split()
for i in range(len(t)):
   t[i] = int(t[i])
s1 = s[t[0]:t[1]+1]
s2 = s[t[2]:t[3]+1]
fw.writelines(s1 + ' ' + s2)
fr.close()
fw.close()