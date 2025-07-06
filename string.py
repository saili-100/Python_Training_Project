# Strings
# strings can be wrriten in single quote, double quote,triple quote
# Question My name is "Suraj"
print("My name is 'Suraj'")
# slicing start end step
str1 = "Hello"
print(str1[::-1])
print(str1[0:3])
print(str1[::2])
print(str1.upper())
# strip remove space from beginning and end
my_str = " India is my country.   "
print(len(my_str))
print(len(my_str.strip()))
# contactenate 
first_name = "Suraj"
last_name = "Deore"
print(first_name + "\n" + last_name)
a=10;b=20
print(a,b)
# print(b)
#  \' ---> print()
# print('It\'s me') 
# print('It\s me') 
# \r --->remove beginning part
# print('It\rs me') 
# \t ----> moves 4 steps ahead
str1='It me   !\t'# 8-index position of \t + count remaining characters first 8 zala then subtract from next 8 i.e 8-7
print(len(str1.expandtabs()))
print(len(str1)) # len function doesn't calculate \t spaces assume as 1 space only 
# \b eats 1 space back
print('I\bts me')

