#Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loopnum

# num = 0
# while num >= 0:
#     num = int(input("Enter a non negative number : "))

# while True:
#     num1 = int(input("Enter a non negative number : "))
#     if num1 < 0:
#         break


#Check if a given number is a prime number using a for loop.

#prime_num = int(input("Enter a  number : "))
# prime_num = 43
# count = 0
# for i in range(1,prime_num + 1):
#     if ( prime_num % i == 0):
#         count += 1

# if(count == 2): 
#     print("Prime")
# else:
#     print("Not Prime")

#-------------------------------------------------------------------
#Second approach
print("2 approach")
prime_num = 15
isPrime = False
if prime_num in [0,1]:
    print("Not a Prime Number")

else:
    for i in (2 ,prime_num):
        if prime_num % i == 0:
            isPrime = True
            print( prime_num," Not prime at 38")
            break

    if (isPrime == False):
         print( prime_num," Prime  at line 42")

#------------------------------------------------------------------------------

print("3 approach")
#not working for 9 15 21
isPrime = False
if prime_num in [0,1]:
    print("Not a Prime Number")

else:
    for i in (2 ,(prime_num // 2 )+ 1):
        if prime_num % i == 0:
            isPrime = True
            print( prime_num," Not prime at 57")
            break

    if (isPrime == False):
         print( prime_num ,"Prime at line 61")


#-------------------------------------------


#approach 4
prime_num = 5
isPrime = False
if prime_num in [0,1]:
    print("Not a Prime Number")

else:
    for i in (2 , int(prime_num ** 0.5 )+ 1):
        if prime_num % i == 0:
            isPrime = True
            print(" Not prime at 74")
            break

    if (isPrime == False):
         print( prime_num ,"Prime at line 77")

