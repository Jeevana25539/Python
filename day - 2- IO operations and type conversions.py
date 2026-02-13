"""# read input numbers from user
num = input()
print(type(num)) # checking the type of number
print(num)"""


"""#implicit Type conversion

num1 = int(input())
val = float(input())
print(type(num1),type(val)) #checking the type of number
res = num1+val
print(res)"""


"""#num1 = input()   # read string type number
print(type(num1))# checking the type of number
res = num1 +10# TypeError: can only concatenate str (not "int") to str
>>> 
print(res)"""


"""# To overcome the above problem by using the explicit type conversion 
num1 = input()   # read string type number
print(type(num1))# checking the type of number
res = int(num1) +10# TypeError: can only concatenate str (not "int") to str
print(res)"""

# converting integer into float 
num = 12
print(float(num))
print(str(num))
print(bool(num))



