import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# Ввод, если два числа и более в одну строку
for i in range(5):
    (a, b ,c) = [int(s) for s in input().split()]
    if b<=59 and a <=23 and c<=59:
        print('YES')
    else:
        print('NO') 