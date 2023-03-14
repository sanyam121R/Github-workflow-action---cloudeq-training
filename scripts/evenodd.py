import sys

def evenodd(a, b):
    if int(a)%2==0 or int(b)%2==0:
        print("Even")
    else:
        print("Odd")

# l = list(map(int, input().split()))
a = int(sys.argv[1])
b = int(sys.argv[2])

evenodd(a, b)