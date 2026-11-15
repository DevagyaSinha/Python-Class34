def paths(m,n):
    if m==1 or n==1:
        return 1 
    return paths(m-1,n)+paths(m,n-1)

input("paths(n,m) counts the number of ways moving left and down ")
print("paths(4,4)=",paths(4,4))
print("paths(4,23)=",paths(4,23))