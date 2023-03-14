def evenodd(l):
    for i in l:
        if i%2==0:
            print("Even")
        else:
            print("Odd")

l = list(map(int, input().split()))
evenodd(l)