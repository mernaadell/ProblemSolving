from operator import itemgetter
if __name__=="__main__":
  t=int(input())
  while(t>0):
    t=t-1
    flag=0
    n=int(input())
    li=[0]
    li2=[0]
    for i in range(n):
      a,b=input().strip().split()
      li.append(int(a))
      li2.append(int(b))
  
    xb=list(zip(li,li2))
    
    xb=sorted(xb, key=itemgetter(0,1))
    
    if(len(xb)==1):
      print("yes")
    s=""
    for i in range(len(xb)-1):
      if(xb[i][1]<=xb[i+1][1]):
        #print("x",(xb[i+1][0]-xb[i][0]))
        for k in range (xb[i+1][0]-xb[i][0]):
          s=s+"R"
        #print((xb[i+1][1]-xb[i][1]))
        for j in range (xb[i+1][1]-xb[i][1]):

          s=s+"U"
          
      else:
        
        flag=1
    if(flag==1):
      print("NO")
    else:
      print("YES")
      print(s)

  


