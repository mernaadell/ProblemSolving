
import numpy 

if __name__ == '__main__':
    n = int(input())
    j=1
    arr = list(map(int, input().rstrip().split()))
    for j in range(n):
        key=arr[j]
        i=j-1
        while i>=0 and key<arr[i]:
            arr[i+1]=arr[i]
            i=i-1
            for col in arr:
                print(col,end=" ")
            print()
        arr[i+1]=key
    for col in arr:
        print(col,end=" ")
            
        