
#Problem solving day-1

# 1) Print given number is positive  or Negative or zero

#number = float(input("Enter a number : "))
number = 4
if number == 8:
    print("Zero")
elif(number > 0):
    print("Positive")
else:
    print("Negative")

#-------------------------------------------------
# 2) Print given number is odd or even

even_odd_number = 3

if even_odd_number % 2 == 0:
    print("Even")
else:
    print("Odd")

#---------------------------------------------------

# 3)  a pesion is eligible to vote or not

age = 19

if age >= 18:
    print("Person is eligible to vote")
else:
    print("Not eligible to Vote")

#------------------------------------------------------------

# 4) find greatest of two numbers

first_number = 21
#                                      int(input("Enter first number : "))
second_number = 33
#                                      int(input("Enter first number : "))
if( first_number  > second_number):
    print(first_number)
else:
    print(second_number)
#----------------------------------------------------------------

# 5) Sudent marks results

student_marks = 39

if( student_marks >= 40 ):
    print("Pass")
else:
    print("Fail")

# --------------------------------------------------------

# 6)

day_num = 1

if (day_num == 1):
    print("Monday")
elif ( day_num == 2 ):
    print("Tuesday")
elif( day_num == 3 ):
    print("Wedensday")
elif( day_num == 4 ):
    print("Thursday")
elif( day_num == 5 ):
    print("Friday")
elif( day_num == 6 ):
    print("Saturday")
elif( day_num == 7 ):
    print("Sunday")
else:
    print("Invalid Input")

#----------------------------------------------------------

# calculator

# first_operand = int(input("Enter first number :"))
# operator =  input("Enter an operator : ")
# second_operand = int(input("Enter second number :"))

# if(operator == "+"):
#     print(first_operand + second_operand)
# elif(operator == "-"):
#     print( first_operand - second_operand)
# elif(operator == "*"):
#     print( first_operand * second_operand)
# elif(operator == "/"):
#     if second_operand == 0 :
#         print("Division by zero is not possible")
#     else:
#         print( first_operand / second_operand)
# else:
#     print("Invalid Input")


first_operand = int(input("Enter first number :"))
operator =  input("Enter an operator : ").lower()
second_operand = int(input("Enter second number :"))

if(operator  in ['add', '+']):
    print(first_operand + second_operand)
elif(operator in ['sub', '+']):
    print( first_operand - second_operand)
elif(operator in ['mul', '*']):
    print( first_operand * second_operand)
elif(operator in ['div', '/']):
    if second_operand == 0 :
        print("Division by zero is not possible")
    else:
        print( first_operand / second_operand)
else:
    print("Invalid Input")


#--------------------------------------------------------------

day_num = 1

if (day_num == 1):
    print("Jan")
elif ( day_num == 2 ):
    print("Feb")
elif( day_num == 3 ):
    print("Mar")
elif( day_num == 4 ):
    print("Aprl")
elif( day_num == 5 ):
    print("May")
elif( day_num == 6 ):
    print("Jun")
elif( day_num == 7 ):
    print("July")
elif( day_num == 8 ):
    print("Aug")
elif( day_num == 9 ):
    print("Sep")
elif( day_num == 10 ):
    print("Oct")
elif( day_num == 11 ):
    print("Nov")
elif( day_num == 12 ):
    print("Dec")
else:
    print("Invalid input")