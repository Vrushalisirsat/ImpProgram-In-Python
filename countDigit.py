# Q. WAP to count Digits in a Number.

# __main__

n=int(input("Enter a Number :"))

m=n
counter=0
while n>0:
    n=n//10
    counter=counter+1
#end of while loop
print("No. Of Digits in Number", m,"=", counter)

#end of __main__
