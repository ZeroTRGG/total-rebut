import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
b=[int(j) for j in input().split()]
b.sort()
print(" ".join([str(i) for i in b]))