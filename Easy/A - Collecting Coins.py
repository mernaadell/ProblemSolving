

if __name__ == "__main__":
    t=int(input())
    while(t>0):
      
      
      a,b,c,n=input().strip().split()
      a=int(a)
      b=int(b)
      c=int(c)
      n=int(n)
      x=max(a,b,c)
      

      if(n>=0):
        a=x-a
        s1=n-(a)
        if(s1<0):
          print("NO")
          continue
          
        else:
          n= n-(a)

      if(n>=0):
          b = x - b
          s2 = n - (b)
          if (s2 < 0):
            print("NO")
            continue
            
          else:
            n=n - (b)


      if(n>=0):
        c = x - c
        s3 = n - (c)
        if (s3 < 0):
          print("NO")
          continue
          
        else:
          n=n - (c)
       
      if(n>=0):
        
        if(n%3==0):
          
          print("YES")
        else:
          print("NO")
      
    
  
 
            
            
 
