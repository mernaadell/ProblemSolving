from operator import itemgetter
if __name__=="__main__":
  t=int(input())
  while(t>0):
    t=t-1
    h,m=input().strip().split()
    h=int(h)
    m=int(m)
    print(((24-h)*60)-m)
