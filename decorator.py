# Decorators
def simple_function():
    print("i am simple")
 
simple_function()
 
###
#  for decorator we have two func outer inner in outer fun reference of func to be decorated.
def my_decorator(func):
 
    def wrapper():
        print("before func call")
        func()  # call to simple_function
        print("after func call")
    return wrapper
 
# use
decorated_function = my_decorator(simple_function)
decorated_function() #calling inner function directly
 
###########
 
 
def my_decorator(func):
 
    def __inner(num1, num2): # so here also two parameters
        if num2 == 0:
            print("cant divide by 0, please provide different value")
            return
        else:
            division = func(num1, num2) # becoz div is returning something
            return division
    return __inner
 
 
@my_decorator
def div(a, b): # here two parameters
    return a/b
 
 
print(div(10, 0))