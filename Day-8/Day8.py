# sum of each even digit in the  element in array
list1 = [202,89,112,8341]
list2 = []

def sumofDigit(num):
    sum = 0
    while num > 0:
        rem = num % 10
        if rem % 2 == 0:
          sum = sum + rem

        num = num // 10
    return sum

for i in list1:
    list2.append(sumofDigit(i))

print(list2)
#------------------------------------------------------------------------------------------------------



def searchElement(arr2 , arr1): 
    for i in arr2:
        if i == arr1:
            return True
    return False

#Liner search algorithm  => O(1)-- S.C, O(n)--T.C

def searchElementIndex(arr2 , arr1): 
    for i in range(len(arr2)):
        if arr2[i] == arr1:
            return i
    return -1

arr1 = 51
arr2 = [2,4,3,1,7,5,15]

if arr1 in arr2:
    print("YES")
else:
    print("No")

print(searchElementIndex(arr2 ,arr1))

print(searchElement(arr2 ,arr1))

#-------------------------------------------------------
# is subset
arr1 = [1,3,4,5,2]
arr2 = [2,4,3,1,7,5,15]

# set1 = set(arr1)
# set2 = set(arr2)
# print(set1.issubset(set2))

def check_subset(arr1 ,arr2):
    for i in arr1:
        if i not in arr2:
            return False
    return True

print(check_subset(arr1, arr2))


def check_without_not_in(arr1 ,arr2):
    for i in arr1:
        flag = False
        for j in arr2:
            if i == j:
                flag = True

        if flag == False:
            return False
    return True

arr1 = [1,3,4,5,2]
arr2 = [2,4,3,1,7,5,15]

print(check_without_not_in(arr1,arr2))


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
max_val = nested_list[0][0]
min_val = nested_list[0][0]
for i in nested_list:
    for j in i:
        total += j
        if (max_val < j):
            max_val = j
        if (min_val > j):
            min_val = j  

print(total)
print(max_val)
print(min_val)