# sum and max min of the list items
list1 = [4,6,7,9,1,-4,3,2]
sum = 0
max_value =  float('-inf') #list1[0]
min_value = float('inf')
for i in list1:
    sum += i
    if max_value < i:
        max_value = i
    if min_value > i:
        min_value = i

print("Sum Of the list is : " ,sum)
print("max_value Number is : ",max_value)
print("Min Number is : ",min_value)

#--------------------------------------------------
list2 = [4,6,7,9,1,-4,3,2]
print(list2)
temp_list = []
for i in range (len(list2)-1 , -1,-1):
   temp_list.append(list2[i])

print(temp_list)
#-----------------------------------------------
list4 = [4,6,7,9,1,-4,3,2]
print(list4)
temp = []
for i in list4:
    temp.insert(0,i)

print(temp)
#-----------------------------------------------------
list3 = [5,8,9,6,4,5,6,8]
print(list3)
low = 0
high = len(list3)-1

while low < high:
    # list3[low] ,list3[high] = list3[high],list3[low]
    list3[low] = list3[low] + list3[high]
    list3[high] = list3[low] - list3[high]
    list3[low] = list3[low] - list3[high]
    low += 1
    high -= 1
print(list3)

