import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
N = int(input())
x1 = 0
if N > 0:
    if N % 2 == 0:
        print('YES')
        print(N + 2)
    else:
        print('NO')
        print(N + 1)
elif N == 0:
    if N == 0:
        print('NO')
        print(N+2)
elif N  < 0:
    print('NO')
    print('2')