## Write a program that asks the user for their name and age ##
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name} you are {age} years old.")


## Q2 sum, difference, product, and quotient ##
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

sum = a+b
print("Sum = ", sum)
diff = a-b
print("Difference = ", diff)
prod = a*b
print("Product = ", prod)
quot = a/b
print("Quotient = ", quot)


## Ask the user to enter two integers and one float. Convert them all to floats and print their average ##
c = int(input("Enter the first integer: "))
d = int(input("Enter the second integer: "))
e = float(input("Enter the float: "))

c = float(c)
d = float(d)
average = (c+d+e)/3
print("Average = ", average)


## Convert string to integer, float and then back to string ##
str1 = input("Enter a number:")

str1 = int(str1)
print("Type of string now is ", type(str1))
str1 = float(str1)
print("The type of string now is ", type(str1))
str1 = str(str1)
print("The type of string now is ", type(str1))


## Swap values ##
a1 = int(input("Enter the first number: "))
a2 = int(input("Enter the second number: "))

temp = a1 
a1 = a2
a2 = temp 
print("Value of first number now is: ", a1)
print("Vlaue of the second number now is: ", a2)

## Celsius to Farenheit ##
celsius = input("Enter the temperature in celsius: ")
celsius = float(celsius)
farenheit_temp = (celsius*(9/5)) + 32
print("The temperature in farenheit is : ", farenheit_temp)


## Take a decimal input and output its integer part annd fractional part individually ##
x = float(input("Enter a floating number: "))

integer = int(x)
fractional_part = x-integer

print(f"The integer part is {integer} and the fractional part is {fractional_part}")