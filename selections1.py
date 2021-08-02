n=int(input("enter num : "))
for i in range(1,n+1):
    size=len(str(i))
    sum=0
    k=i
    while(k>0):
        ones=k%10
        sum+=ones**size
        k=k//10
    if(i==sum):
        print(sum)
        

   

