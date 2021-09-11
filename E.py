import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
b=int(input())
s=o=0
while not a==b==0:
    a=b
    b=int(input())
    if b==a:
        s+=1
        if s>o:
            o=s
    else:
        s=1
print(o)