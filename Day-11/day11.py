
#bubble sort 
#ascending 
list1 = [1,-5,-34,6,8,12,4]

for j in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+ 1] = list1[ i + 1] ,list1[i]
    print(list1)


list2 = ["", "vineeth" ,"kumar" , "run" , "aravindkumar","sairam"]


for j in range(len(list2)-1):
    for i in range(len(list2)-1- j):
        if len(list2[i]) > len(list2[i + 1]):
            list2[i],list2[i+ 1] = list2[ i + 1] ,list2[i]
    
    print(list2)


list3 = [[1,2,3],[-5,7],[-8,9 ,11 ,-32]]


for j in range(len(list3)-1):
    for i in range(len(list3)-1- j):
        if (list3[i][0]) > (list3[i + 1][0]):
            list3[i],list3[i+ 1] = list3[ i + 1] ,list3[i]
    print(list3)


         


    #[[-8 ,9 ,11 -32],[-5,7] ,[1,2,3]
