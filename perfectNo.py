# WAP to read a number from user and check it is perfrct number or not.
# eg:->  6=> 1+2+3=>6  ............(if no. which is divisible by no and their sum called perfect no.).

#__main__

n=int(input("Enter a Number :"))

sum=0
i=1
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
    #end of if
#end of while loop

if n==sum:
    print("Perfect Number")
else:
    print("Not a perfect Number")

#end of __main__