fr = open('rosalind_ini6.txt','r')
fw = open('rosalind_ini6.res.txt','w')
s = fr.readline()
s = s.split()
dict = {}
for i in range(len(s)):
    dict[s[i]] = 0
for i in s:
    dict[i] = dict[i] + 1
for key, value in dict.items():
    fw.write(key + ' ' + str(value) + '\n')
fr.close()
fw.close()