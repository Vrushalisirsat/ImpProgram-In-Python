# Q.WAP to calculate a power of number.

#__main__

n=int(input("Enter a number :"))
p=int(input("Enter a power :"))

i=1
power=1
while i<=p:
    power=power*n
    i=i+1
#end of if
print("Power of",n,"to the power",p,"=",power)
#end of __main__
