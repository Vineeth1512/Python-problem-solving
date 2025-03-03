# num = 20
# sum =0

# print(num * (num +1) /2)

# for i in range(1, num +1):
#     sum += i

# print(sum )


# # O(1) Time complexity
# # O(logn) - Binary search
# # O(n) Linear time complexity
# # O(n sqaure)    10 square tumes ex two for loops
# # O (nlogn)
# # O(n cube)  1000 times increase



# num = 121
# temp = num
# rev = 0
# while num > 0:
#     rem = num % 10
#     rev = rev *10 + rem
#     num = num // 10

# print(rev)

# if (temp == rev):
#     print("Polindrome")
# else:
#     print("Not Polindrome")

# teams_num = int(input("Enter a number : "))
# sum = 0
# for i in range(1 ,teams_num+1):
#     if i % 2 == 0:
#         sum += (i * 100)
#         print(sum)

# print("Total allocated budged is :" , sum)
#--------------------------------------------------------------------------------
# perfect Number 
# 6 ,28 ,496 8128
perfect_num = 8128
sum = 0
for i in range(1,perfect_num):
    if perfect_num % i == 0:
        sum += i

if perfect_num == sum:
    print("Perfect Number")
else:
    print("Not Perfect")
#------------------------------------------------------
# GCD


num1 = 13
num2 = 3

while num2 !=0:
    rem = num1 % num2
    num1 = num2 
    num2 = rem

print("GCD ", num1)

#-------------------------------------------------------------------
num1 = 12
num2 = 18


max_num = num1 if num1 > num2 else num2

# while True:
#     if max_num % num1 == 0 and max_num % num2 == 0:
#         print("Lcm of two nubers is ", max_num)
#         break
#     max_num +=1

for i in range(max_num , (num1  *  num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        print(i, " is the LCM ")
        break

#---------------------------------------

# sum of non prime numbers

sum = 0
for i in range(1 , 10):
    count = 0
    for j in range( 1 , 10):
        if i % j == 0:
            count +=1
    if count != 2:
       sum += i 
    
print("sum of non prime numbers : ",sum)