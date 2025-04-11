#Binary search algoritham it works on sorted conditions
#TC :logN
def binary_search(input_list,search_elem):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid =(low + high) // 2
        if input_list[mid]==search_elem:
            return mid
        elif input_list[mid] > search_elem:
            high = mid - 1
        else:
            low = mid + 1
    return -1

list1 = [9,8,7,6,5,4,3,2]
search_elem = 33


# print(binary_search(list1 ,search_elem))
# def desecending_order(list1):
#     for i  in range(len(list1)):
#         if list1[i]> list1[i-1]:
#             return False
#     return True
# print(desecending_order(list1))

def ascending_order(list1):
    for i in range(1,len(list1)):
        if list1[i] < list1[i-1]:
            return False
        
    return True

print(ascending_order(list1))

list2 = [1,2,1,2,3,5,8,5]

visit_method = []
set1 = set()

for i in list2:
    if i in visit_method:
        set1.add(i)
    else:
        visit_method.append(i)

# print(list(set1))

# print(visit_method)