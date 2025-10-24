# lambda func 
# it is anonymous function
# lamba args:expression   many args but only one expression 
# x = lambda a:a+10
# print(x)  #<function <lambda> at 0x000001A7BE851440>
# print(type(x)) #<class 'function'>
# print(x(5))

greet_user = lambda name: print("Hey there",name)
good_name = input("Enter name")
greet_user(good_name)