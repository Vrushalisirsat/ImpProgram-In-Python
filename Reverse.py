# Q. WAP to read a number(integer number) and Reverse the number.

n=int(input("Enter a number : "))


revs=0

while n>0:
    a=n%10                     #It will find the last digit
    revs=revs*10 + a           #It will give you a reverse
    n=n//10                    #It will reverse the last digit
#end of loop
print("Reverse = ",revs)
#end of __main__


