import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
x = input()
xs = False
if x[0] == '-':
    xs = True
    x = x[1:]
x = x[::-1]
if xs:
    x = '-' + x
print(int(x))
