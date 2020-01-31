if __name__=="__main__":
    t=int(input())
    while t>0:
        t=t-1
        n,d=input().strip().split()
        n=int(n)
        d=int(d)

        if(n<d):
            print("NO")
            continue
        for i in range(n):
            x=i+(d/i+1)
            prev=0
            if x>n:
                print(prev)
                break
            else:
                prev=i



