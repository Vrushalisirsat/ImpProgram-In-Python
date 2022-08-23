# Q. WAP to find Factorial of number.

#__main__

n=int(input("Enter a number : "))

fact=1
i=1

while i<=n:
    fact=fact*i
    i=i+1
#end of loop
print("Factorial = ",fact)
#end of __main__