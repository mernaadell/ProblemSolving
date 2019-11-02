if __name__ == "__main__":

    t=int(input())
    while(t):

        
        pbf=input()
        hc = input()
        x=pbf.split()
        y=hc.split()
        p=int(x[0])
        b=int(x[1])
        f=int(x[2])
        h=int(y[0])
        c=int(y[1])
        equ=(f*2+b*2)
        if equ <= p:
            print(h*b+c*f)
        else:
            i=p//2
            if i*h >=i*c:
                print(i*h)

            else:
                print(i*c)
        t-=1







