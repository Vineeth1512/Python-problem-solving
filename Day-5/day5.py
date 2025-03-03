# sum of add digits in given number

num = 2355
sum = 0
while num > 0:
    rem = num % 10
    if(rem % 2 != 0):
        sum +=rem

    num = num // 10

print("sum of odd numbers " , sum)


# Sum of non prime numbers 

def isPrime( input_num):
    for i in range(2 ,input_num):
        if input_num % i == 0:
            return False
    
    return True

num1 = 3436
sum = 0
while num1 > 0:
    rem = num1 % 10 
    count = 0
    preme_res = isPrime(rem)
    if(preme_res == False):
     sum += rem 
    num1 = num1 // 10

print("Non Primes sum is  " ,sum)


n = 100
for i in range(2, n + 1):
    if isPrime(i):
        print(i)




print("With out function")
for i in range(1, 20):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)

    


# ArmStrong Number

arm_num = 9474
temp = arm_num
arm_sum = 0
str_num =  str(arm_num)

while arm_num > 0:
    digit = arm_num % 10
    arm_sum += digit ** len(str_num)
    arm_num = arm_num // 10

if temp == arm_sum: 
    print("ArmStrong number ",arm_sum)
else:
    print("Not arm strong")


def check_armstrong(arm_num):
    temp = arm_num
    arm_sum = 0
    str_num =  str(arm_num)
    while arm_num > 0:
        digit = arm_num % 10
        arm_sum += digit ** len(str_num)
        arm_num = arm_num // 10

    if temp == arm_sum: 
       return True
    else:
        return False

min_num = 100 
max_num = 10000
# print arm strong numbers up to nth number

for i in range(min_num , max_num + 1):
    if(check_armstrong(i)):
        print(i)
        