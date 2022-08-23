# Q. WAP to read a number and check it is prime number or not.

# __main__

n=int(input("Enter a number : "))

counter=0
i=1

while i<=n:
    if n%i == 0:
        counter=counter+1
    #end of if
    i=i+1
#end of loop

if counter == 2:
    print("It is a prime Number :")
else:
    print("It is not a prime Number")

#end of __main__
