def max_sum(A):
 
    max_initial = 0
 
    max_final = 0
 
    for i in A:

        max_final = max_final + i
 
        max_final = max(max_final, 0)
 
        max_initial = max(max_initial, max_final)
 
    return max_initial
 
 
if __name__ == '__main__':
 
    n=int(input("enter size of array: "))
    A=eval(input("enter list"))
 
    print("The largest subarray sum is: ", max_sum(A))