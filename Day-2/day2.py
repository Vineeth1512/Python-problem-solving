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

# check if three sides length form a valid traingle

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


#--------------------------------------

# 5) Implement a menu-driven program where the user can choose to:


while True:
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
        print("Exiting")
        break
    else:
        print("Invalid Option")
#-----------------------------------------------------------------------
# Implement a basic login system where the user has three
 # attempts to enter the correct password using a loop

db_username = "Vineeth1512"
db_password = "Vineeth@123"

total_attempts = 3
while total_attempts > 0 :
    input_username = input("Enter username : ")
    input_password = input("Enter password : ")

    if db_username == input_username and db_password == input_password:
        print("Login Successfull")
        break
    else:
        total_attempts -= 1
        print("Login failed you still have ",total_attempts ,"attempts remaing")