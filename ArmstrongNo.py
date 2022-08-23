# Q. WAP to read a number from the user and check the number is Armstrong number or not.
#  eg :->  153 => ((1*1*1 + 5*5*5 + 3*3*3) = 153)

# __main__

N=int(input("Enter a Number :"))
m=N
arm=0

while N>0:
    rem=N%10
    arm=(rem*rem*rem)+arm
    N=N//10
#end of while loop
print("New Update Armstrong Number : " ,arm)

if m==arm:
    print("It is a Armstrong Number")
else:
    print("It is not a Armstrong Number")
#end of if
# end of __main__


