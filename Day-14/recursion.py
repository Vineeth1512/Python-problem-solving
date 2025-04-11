# def exp( a , b):
#     if b ==0:
#         return 1
#     return a * exp( a ,b -1)

# print(exp(2,4))
# def str_rev(str1):
#     if len(str1)<=0:
#         return str1
#     return str1[-1]+str_rev(str1[0:len(str1)-1])
# str="vineeth"
# # print(str[0:len(str)-1])
# print(str[-1])
# print(str_rev("vineethkumar"))

# Reversing the List 
def list_rev(list1):
    if len(list1)<=0:
        return list1
    return list1[-1 :]+list_rev(list1[0:len(list1)-1])
list1=[3,4,56,7]
print(list_rev(list1))

