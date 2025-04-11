list1 = [5,7,8,6,4,3,12,43]

# list1.sort()

# print(list1[-2])

list_max = float('-inf')
second_max = float('-inf')

for i in list1:
    if i  > list_max:
        list_max = i

print(list_max)

for i in list1:
    if i > second_max and i !=list_max:
        second_max = i

if second_max !=float('-inf'):
    print(second_max)
else:
    print("No second Max")


#-----------------------------------------------------
list2 = [20,15,26,2,98,6]
list3 =sorted(list2)
list4 = []
output_list = []
for i in list2:
    output_list.append(list3.index(i)+1)

print(output_list)
#----------------------------------------------------------
print(list2)
print(list3)
for i in list2:
    for j in range(len(list3)):
        if i == list3[j]:
             list4.append(j+1)
   



print(list4)

#Nth Largest Element
a = [4, 2, 6, 7, 8, 6, 3, 24, 13]
nth = 2

# Sort manually in descending order
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]  # Swap

    if i == (nth - 1):
        print(a[i])
