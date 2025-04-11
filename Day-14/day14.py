#print n natural numbers
def n_natural_numbers(input_num):
    if input_num == 0:
        return
    n_natural_numbers(input_num - 1)
    print(input_num)

n_natural_numbers(10)


def sum_of_digits(input_num):
    if input_num == 0:
        return 0
    return input_num % 10 + sum_of_digits(input_num // 10)

print("sum of digits is ",sum_of_digits(12345))


def exponent(a ,b):
    if a == 0 or b == 0:
        return 1
    return a * (exponent(a,b -1))

print("expontential is ",exponent(3,3))



def fibonaci(n):
    if n <= 1:
        return 1
    
    return fibonaci(n -1) + fibonaci( n - 2)

print(fibonaci(4))



#reverse a string using 
# h + reverse("vineet")

def reverseString(str):
    if len(str) <=0:
        return str
    return str[-1] + reverseString(str[0 : len(str)-1])

print(reverseString("vineeth"))

list1 = [4,6,7,8,9]

def reverseList(str):
    if len(str) <= 0:
        return str
    return str[-1 :]  + reverseList(str[0 : len(str)-1])

print(reverseList(list1))
