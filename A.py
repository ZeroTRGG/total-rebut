import sys
import math
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
(A,B,C) = [int(s) for s in input().split()]
(H,L) = [int(s) for s in input().split()]
n=(A*B+A*C+B*C)*2-A*B
n=n-0.15*n
m=H*0.001
p=L*0.001
j=m*p
j=j-0.1*j
u=n/j
print(math.ceil(u))