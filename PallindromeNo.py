# Q.WAP to read a number and find the pallindrome of given number.

# __main__


n=int(input("Enter a Number : "))
m=n
rev=0

while n>0:
    a=n%10          #It will find the last digit
    rev=(rev*10)+a
    n=n//10          #It will reverse the last digit
#end of loop

print("Reverse = ",rev)

if rev == m:
    print("It is Pallindrome Number")
else:
    print("It is Not a Pallindrome Number")

#end of __main__