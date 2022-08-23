# Q. WAP to find sum of Digits of a Number.
# eg :->   n=126 => 1+2+6 => 9

# __main__

n=int(input("Enter a number :"))

sum=0
while n>0:
    rem=n%10           #for find/get the last digit of our number
    sum=sum+rem         # for getting the sum of our digit
    n=n//10             # for getting remaining digit
#end of while loop
print("Sum of digit of Number =",sum)

