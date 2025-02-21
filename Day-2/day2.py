#Medium questions 
# 1) find greatest of three numbers

first_number = 5
second_number = 4
third_number = 3


if ( first_number > second_number and  first_number > third_number):
    print(first_number)
elif(second_number > third_number and second_number > first_number):
    print(second_number)
else:
    print(third_number)




# -------------------------------------------------------------

# heck if three sides length form a valid traingle

a = 3
b = 6
c = 4

if (( a + b > c) and (b + c > a) and( a + c > b )):
    print("Valid traingle")
else:
    print("Invalid traingle")

#-------------------------------------------------------------------
#Leap year 

year  = 100

if ( year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print("leap year")
else:
    print("not leap year")


#--------------------------------------------------------------------
#character entered by the user as a vowel, consonant, or neither.

user_input = "A".lower()

if len(user_input) == 1:
    if user_input in "aeiou":
        print("Vowel")
    elif user_input.isalpha():
        print("Constants")
    else:
        print("Special characters or numbers")
else:
    print("Invalid Input")

# --------------------------------------------------------------------------------


#lOOPS

# 1) Print all numbers from 1 to 100 using a for loop.

# for i in range(1,101):
#     print(i)
#-----------------------------------------------------------------

#  2) Write a program to print the sum of the first n natural numbers.



# user_input = int(input("Enter a number : "))

# sum = 0
# for i in range(user_input + 1):
#    sum =  user_input * ((user_input + 1)/2)

# print("Sum is : ",sum)



#---------------------------------------------------------------------
#  3) Print all even numbers between 1 and 50 using a while loop.



# even_number = 1
# while( even_number < 50):
#     if even_number % 2 == 0:
#         print(even_number)
#     even_number += 1



# ----------------------------------------------

# 4) Write a program to display the multiplication table of a given number. First 20

# n = int(input("Enter Multiplacation Number : "))
# for i in range(1,21):
#     print ( n ,"x", i ,"=" , n * i)

print("--------------------------------------------------")

#----------------------------------------------------------------------------------

# 5) Reverse a number using a while loop

num = 123
rev = 0

while(num > 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10


print("Reverse of given number is : ",rev)
num = 321
sum = 0
while(num > 0):
    rem = num % 10
    sum += rem
    num = num // 10

print("Sum of given number is : ",sum)


# -----------------------------------------------------------
print("-------------------------------------------------------------------------")

# 6) Write a program to count the number of digits in a given number using a while loop

num = 32154
count = 0
while(num > 0):
    rem = num % 10
    count += 1
    num = num // 10

print("Count  of given number is : ",count)

# -----------------------------------------------------------------------

# Medium  for loops 

# 1) Print the first 10 terms of the Fibonacci series using a for loop

a = 0 
b = 1
print(a)
print(b)
for i in range(1,11):
    c = a + b
    a = b
    b = c
   
    print(c)
#---------------------------------------------------------------------

# 3) Write a program to calculate the factorial of a number using a while loop

num = 4
fact = 1
while(num > 0):
    fact = fact * num
    num -= 1
print("Factorial of given nuber is : " ,fact)

# -----------------------------------------------------------------------

# 4) Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop
#i % 15 == 0 or 
for i in range(1 ,101):
    if( i % 3 == 0 and i % 5 == 0):
        print(i)

#--------------------------------------

# 5) Implement a menu-driven program where the user can choose to:


print("1. Find the square of a number.")
print("2. Find the cube of a number.")
print("3. Exit")
choose_option = int(input("Choose an option from above : "))

if choose_option == 1:
    square_num = int(input("Enter the number to square : "))
    print(square_num ** 2)
elif choose_option == 2:
    square_num = int(input("Enter the number to cube : "))
    print(square_num ** 3)
elif choose_option == 3:
    print("Exit")
else:
    print("Invalid Option")