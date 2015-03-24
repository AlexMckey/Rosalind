fr = open("rosalind_fib.txt",'r')
fw = open("rosalind_fib.res.txt",'w')

st = fr.read().strip().split()
n = int(st[0])
k = int(st[1])

def fib(n,k):
    a, b = 1, 1
    i = 1
    while i < n:
        print b,
        a, b = b, b+k*a
        i = i + 1

fb = fib(n,k)

fw.write(str(fb))

fr.close()
fw.close()