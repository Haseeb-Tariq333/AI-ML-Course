## CHECK WETHER A STRING IS PALINDROME OR NOT ##
str = input("Enter a string to check if it is palindrome or not: ")

reversed_string = str[::-1]
print(reversed_string)


if reversed_string == str:
    print(f"The string {str} is palindrome")
else:
    print(f"The string {str} is not palindrome")
## Loop method
reversed_str = " "
for char in str:
    reversed_str = char + reversed_str
print(reversed_str)



## COMPUTE AVERAGE OF ALL NUMBERS IN A LIST ##
list1 = [1,2,3,4,5]
sum = 0
for val in list1:
    sum += val
average = sum/len(list1)
print(average)  



## Input two integers list from user and merge then and sort them ##
list1 = []
list2 = []

a1 = int(input("Enter integer for list1: "))
list1.append(a1)
a2 = int(input("Enter integer for list1: "))
list1.append(a2)
a3 = int(input("Enter integer for list1: "))
list1.append(a3)
b1 = int(input("Enter integer for list2: "))
list2.append(b1)
b2 = int(input("Enter integer for list2: "))
list2.append(b2)
b3 = int(input("Enter integer for list2: "))
list2.append(b3)
print(list1)
print(list2)

new_list = list1+list2
new_list.sort()
print(new_list)



## Make a tuple of even and odd numbers from a given integer typle ##
tup_even = ()
tup_odd = ()
tup = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
for vals in tup:
    if(vals%2 == 0 ):
        tup_even = tup_even + (vals,)
    elif vals%2 != 0:
        tup_odd = tup_odd + (vals,)
print(tup_even)
print(tup_odd)



############################################

dict_students = {}

def add_student():
    add_name = input("Enter the name of the student: ")
    add_marks = input("Enter the marks of the student: ")
    dict_students[add_name] = add_marks 
    print(f"The student {add_name} and its marks have been added to the dictionary")
    print(dict_students)


def update_marks(): 
    update_stu = input("Enter the name of the student for which you want to update the marks: ")
    for key,value in dict_students.items():
        if key == update_stu:
            new_marks = input("Enter the new marks for the student: ")
            dict_students[key] = new_marks
            print(f"The new marks have been updated and the new marks for student {update_stu} are {new_marks}")
            print(dict_students)
 
    
def search():
    search_stu = input("Enter the name of the student which you want to search: ")
    for key,value in dict_students.items():
        if search_stu == key:
            print(f"The marks for the student {search_stu} are {value}")


def display_all():
    print(dict_students.items())
    

def display_meny():
    user_choice = 'A'
    while user_choice != 'E': 
        user_choice = input(" \n A.Add a Student \n B.Update Marks \n C.Search for a student \n D.Display all students \n E.Quit \n\n Enter your choice : ")
        if user_choice == 'A':
            add_student()
        elif user_choice == 'B':
            update_marks()
        elif user_choice == 'C':
            search()
        elif user_choice == 'D':
            display_all()
        elif user_choice == 'E':
            print("Quitting the program....Goodbye")
        else:
            print("Enter a correct choice")

display_meny()


## Create a dictionary that maps each word to its length.
dict_words = {}
words = ["apple", "banana", "kiwi", "cherry", "mango"]
for value in words:
    dict_words[value] = len(value)
print(dict_words)


## Write a program that takes a string from the user and prints the number of spaces in the string
str_1  = input("Input a string: ")
count = 0
for char in str_1:
    if char == " ":
        count += 1
print(F"Number of spaces in the string are {count}")



## Write a program to check whether two lists share no common elements
list1 = [1, 2, 3, 6]
list2 = [5, 6, 3, 8]
list1 = set(list1)
list2 = set(list2)

common_elements = list1.intersection(list2)
print(f"The two lists share the following common elements: {common_elements}")


## Ask the user for a string and print All unique characters and The count of unique characters
str_2  = input("Input a string: ")
unique_chars = ""
for char in str_2:
    if char not in unique_chars:
        unique_chars += char
print(f"The unique character in string are {unique_chars}")
print(f"The number of unique chars in the string are {len(unique_chars)} ")
        

