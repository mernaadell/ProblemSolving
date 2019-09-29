#https://codeforces.com/contest/1230/problem/A
if __name__ == "__main__":
    a,b,c,d=input().strip().split()
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    if(a+b==c+d or a+c==b+d or a+d==c+b or a+b+c==d or a+b+d==c or a+c+d==b or a+b+c+d==0 or b+c+d==a):
        print("YES")
    else:
        print("No")
 