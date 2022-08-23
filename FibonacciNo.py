# Q. WAP to print first N fibonacci numbers.Read the value of N from user.

n=int(input("Enter the number that you want to find fibonacci number :"))

a=0
b=1
i=1

while i<=n:
    print(a , end=" ")
    c=a+b
    a=b
    b=c
    i=i+1
#end of loop
#end of __main__
