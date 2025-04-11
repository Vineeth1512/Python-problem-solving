def binary_search(input_list,search_elem):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid =(low + high) // 2
        if input_list[mid]==search_elem:
             return True
        elif input_list[mid] > search_elem:
             high = mid - 1
        else:
            low = mid + 1
    return False

list1 = [1,5,10,11,12,19,100]
list2 = [4,5,-2,1]
list3 = []
for i in list2:
   list3.append(binary_search(list1,i))

print(list3)



def duplicate_digit(num):
    duplicate_list = []
    while num > 0:
        digit = num % 10
        if digit in duplicate_list:
            return True
        else:
            duplicate_list.append(digit)
        num = num // 10
    return False

print(duplicate_digit(1234562) )

lis4 = [1234,24,54,777]
d_list = []

for i in lis4:
   d_list.append(duplicate_digit(i))

print(d_list)






def miss_digit(num):
    temp = num
    list1 = []
    while temp > 0:
        digit = temp % 10
        list1.append(digit)
        temp //= 10

    max_in_list = max(list1)
    min_in_list = min(list1)

    for i in range(min_in_list , max_in_list +1):
        if  i not in list1:
             print(i ,end='')
    
num = 34571
miss_digit(num)





list1=[5,10,25,17,20]
min_val = min(list1)
max_val = max(list1)
list2 = []

def isPrime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

for i in range(min_val ,max_val):
    if i not in list1:
        if isPrime(i):
            list2.append(i)

print(list2)