from collections import Counter

fr = open("rosalind_gc.txt",'r')
fw = open("rosalind_gc.res.txt",'w')

dict = {}
for l in fr:
	s = l.strip()
	if s[0] == '>':
		key = s[1:]
		dict[key] = {'pc':0.0,'gc':0,'all':0}
		continue
	cnt = Counter(s)
	dict[key]['gc'] = dict[key]['gc'] + cnt['G'] + cnt['C']
	dict[key]['all'] = dict[key]['all'] + len(s)

for key in dict.keys():
	dict[key]['pc'] = dict[key]['gc'] * 100.0 / dict[key]['all']
	fw.write(key + '\n' + str(dict[key]['pc']) + '\n')
fw.write('\n')

sl = map(lambda x: (x,dict[x]['pc']),dict.keys())
sl.sort(key=lambda x:x[1], reverse=True)

fw.write(sl[0][0] + '\n' + str(sl[0][1]))

fr.close()
fw.close()