def hanoi(n):
    if n==0:
        return 0 
    return 2*(n-1)+1

input("hanoi(n) count the minimum wayss to shift the hanoi disks from a to c ")

print("hanoi(1)=", hanoi(1))
print("hanoi(2)=", hanoi(2))

n=int(input("enter the number of disks"))
print("to transfer",n," numbers of disks will take", hanoi(n))