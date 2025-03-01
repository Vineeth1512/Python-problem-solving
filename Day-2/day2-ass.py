#lOOPS

# 1) Print all numbers from 1 to 100 using a for loop.

for i in range(1,101):
    print(i)


# TC : O(n) , SC : O(1)
#-----------------------------------------------------------------

#  2) Write a program to print the sum of the first n natural numbers.



user_input = int(input("Enter a number : "))

sum = 0
for i in range(user_input + 1):
   sum =  user_input * ((user_input + 1)/2)

print("Sum is : ",sum)



#---------------------------------------------------------------------
#  3) Print all even numbers between 1 and 50 using a while loop.



even_number = 1
while( even_number < 50):
    if even_number % 2 == 0:
        print(even_number)
    even_number += 1



# ----------------------------------------------

# 4) Write a program to display the multiplication table of a given number. First 20

n = int(input("Enter Multiplacation Number : "))
for i in range(1,21):
    print ( n ,"x", i ,"=" , n * i)

print("--------------------------------------------------")


# 4) Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop
#i % 15 == 0 or 
for i in range(1 ,101):
    if( i % 3 == 0 and i % 5 == 0):
        print(i)
