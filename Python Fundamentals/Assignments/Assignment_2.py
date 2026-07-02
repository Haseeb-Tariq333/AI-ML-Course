## Use conditional statements to determine the tax rate based on the salary input by the user ##

salary = int(input("Enter your salary: "))
if salary < 30000:
    print("You will face 5% tax")
elif salary >= 30000 and salary <= 70000:
    print("You will face 15% tax")
elif salary > 70000:
    print("You will face 25% tax")  
    
    
## Take input a and b from user and print even numbers between them ##
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

for i in range(a, b+1):
    if(i%2 == 0):
        print(f"even number : {i}")


## Print digits of a number ##
def print_digits(a):
    digits=[]
    while a > 0:
        b = a%10
        a = int(a/10)
        digits.append(b)
    for digits in reversed(digits):
        print(digits)
print_digits(1234)


## Return the count of number of digits in number n ##
def count_digits(a):
    count = 0
    while a > 0:
        a = int(a/10)
        count += 1
    print(f"Number of digits are {count}")
count_digits(1234) 
  
  
## Function to return the sum of digits of a number n ##
def return_sum(a):
    sum = 0 
    while a > 0:
        b = a%10
        a = int(a/10)
        sum += b
    print(sum)
return_sum(1234)


## WAP a program to print numbers between 1 and 100 divisible by both 3 and 5 ## 
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)
        

## Input from user until user enters quit ##

while True:
    a = input("Enter the number:")
    if a == "quit":
        print("Exiting....Goodbye")
        break
    a= float(a)
    if a>0:
        print("Number is positive")
    elif a<2:
        print("Number is negative")
    else:
        print("Number is zero")


## Check wether a number is prime or not ##
def is_prime(n):
    if n<=2 and n>0:
        return True
    for i in range(2, n-1):
        if n%i == 0:
            return False
        else: 
            return True
print(is_prime(19))