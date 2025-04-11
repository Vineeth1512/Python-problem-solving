n = int(input("Enter a number "))
sum = 0
for i in range(1 ,n + 1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
    

print(sum)

for i in range(n + 1):
    for j in range(n + 1):
        print("*", end=" ")
    print()


list1 = [1,3,5,6,8,9]
max = float('-inf')

for i in range(len(list1)-2):
    triple_max = list1[i]+ list1[i +1] + list1[i + 2]

    if max < triple_max:
        max = triple_max

print(max)