from operator import itemgetter
if __name__=="__main__":
  t=int(input())
  while(t>0):
    t=t-1
    n,k=input().strip().split()
    n=int(n)
    k=int(k)
    x=n%k
    y=n-x
    if(x<(k//2)):
      print(y+x)
    else:
      print(y+(k//2))
