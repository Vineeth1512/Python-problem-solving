num1 = int(input("Enter a number to reverse : "))

def reverse_numver(input_num):

    temp = input_num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return rev

result = reverse_numver(num1)
print(result)





def check_palindrome(input_num):
    temp = input_num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    
    if rev == input_num:
        return True
    else:
        return False


if check_palindrome(num1):
    print("Its Palindrome")
else:
    print("Not Palindorme")



def factorial(input_num):
    fact = 1
    for i in range(1 ,input_num+1):
        fact = fact * i
    return fact

print(factorial(5))


