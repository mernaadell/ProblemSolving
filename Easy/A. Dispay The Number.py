if __name__=="__main__":
    t=int(input())
    while t>0:
        t=t-1
        n=int(input())
        if n%2==1:
            print("7",end="")
            n=n-3
        while n>0:
            print("1",end="")
            n=n-2
            print()

