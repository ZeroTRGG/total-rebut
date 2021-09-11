import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
(M,D) = [int(s) for s in input().split()]
if M<=0 and D<=0:
    print(0)
elif D==2 and M==2:
    print(2)
elif M%2==0 and M%2==0:
    if (M*2)==(D*2):
        print(1)
    elif M>D:
        print(1)
    elif M<D:
        print(2)
elif D%2!=0 and M%2!=0:
    if M>D:
        print(1)
    elif M<D:
        print(2)
elif M%2==0 and D%2!=0:
    if M>D:
        print(1)
    elif M<D:
        print(2)
elif M%2!=0 and D%2==0:
    if M>D:
        print(1)
    elif M<D:
        print(2)
elif M==D:
    print(0)