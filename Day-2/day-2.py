#
# Declaring veriables all data types
#Numeric types

integer_number = 10

floating_number = 3.13

compile_number = 3 + 2j

is_valid = True


#----------------------------------------------------------------------------
# Sequence types 

text = "virat Kumar"

numbers_list = [ 4,6,7,8,9] #list

coordinates = ( 2,5,7,8,4)  #tupple 

range_of_numbers = range(5) 

tupples_content = { 4,6,7,8, " hello"}
#--------------------------------------------------------------------


#Operators
#Arthematic Operators + ,-,*,/,//,

NumOne = 14
NumTwo = 4

print(NumOne + NumTwo)

print(NumOne - NumTwo)

print(NumOne * NumTwo)

print(NumOne / NumTwo)

print(NumOne // NumTwo)

print(NumOne ** NumTwo)


print(NumOne % NumTwo)


#Assignment Operators 
print("Assignment operators")

NumTwo+=10
print(NumTwo)


NumTwo-=10
print(NumTwo)

NumTwo*=10
print(NumTwo)

NumTwo/=10
print(NumTwo)

NumTwo//=10
print(NumTwo)

NumTwo**=10
print(NumTwo)


#Relational operators

print(6 > 8)

print(5 == 3)

print(5 <= 10)

print(3 >= 10)

print(5 != 4)

#logical Operators
print("Logical Operators")


print( 5 < 6  and 7 < 8)

print(True and True)

print(False and (True and False and True))

print(4 and 5)

print (6 and 4)

print( 0 and 4)

print('' and True)

print(1 and [])

print (-1 and -2)

print("vineeth" and "kumar")

#Or Gate 

print("OR Gate")
print( False or False)

print(True or True)

print( False or True)

print(2 or 3)#2

print( 3 or 2)#3

print(0 or 2 )#2
print(2 or 0) #2

print('' or True)
print(' ' or True)
print(1 or [])

print(-1 or -2)

#Not Operators




#Bitwise operators & | ^ ~ >> <<

print(2 & 4)

# 0010
# 0100
# 0000
# (Or ) |
print(13 | 15)
# 1101
# 1111
# 1111
print(13 ^ 15)
# 0010



#------------------------------------------------------------------------
# conditional statements
# num1 = int(input("Enter Number"))
num1 =32
if num1 > 0:
    print(num1,"Is positive")
else:
    if num1 ==0:
        print(num1)
    else:
        if num1 == -1:
            print(num1)
        else:
            print(num1,"Is negative") 


#foor loop

for i in range(1,25):
    if i % 2 ==0:
        print(i)


#while loop
clls=1
while clls <= 10:
    roll=1
    while roll <31:
     print(clls , roll)         
clls += 1

# break and continue

for i in range(0,11):
    if i==5:
        break
    print(i)


for i in range(0 ,11):
    print(i)
    print(i)
    if i >=5:
        break
    print(i)
 
# functions

def greatest_number(num1 , num2):
    if(num1 > num2):
        print(num1)
    else:
         print(num2)


greatest_number(num2 = 100 ,num1 = 20)


def find_greatest(num1 ,num2):
    if(num1 > num2):
        return num1 , 34,56 ,"Vineeth" ,True, 2+2j, 5.567
    else:
        return num2

result = find_greatest(15,10)





