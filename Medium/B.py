if __name__=="__main__":
    t=int(input())
    while(t>0):
        t=t-1
        ans=0
        n = int(input())
        while(n>=10):
            x=n//10
            n=n%10+x
            ans =ans+x*10
        print(ans+n)


