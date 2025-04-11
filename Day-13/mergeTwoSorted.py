list1 = [1,3,5,7,9,11]
list2 = [2,4,7,8,9,10]
# merge two sorted lists in one list
list3 = []
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
list3.sort()
print(list3)

low1 , low2 = 0 , 0
sored_list = []
while low1 < len(list1) and low2 < len(list2):
    if list1[low1] < list2[low2]:
        sored_list.append(list1[low1])
        low1 += 1
    else:
        sored_list.append(list2[low2])
        low2 += 1

sored_list.extend(list2[low2 : ])
sored_list.extend(list1[low1 : ])

print(sored_list)


#recursion 

def factorial(input_num):
    if input_num == 1 or input_num == 0:
        return 1
    return input_num * factorial(input_num -1)

print(factorial(5))