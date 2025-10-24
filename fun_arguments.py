# positional arguments
# default arguments
#  Keyword arguments
# variable positional arguments *args
# variable keyword arguments **kwargs
# func an argument 
# Inner func 

# 1. positional arguments
# def my_function(a,b): # defining the function 
    # print(a)
    # print(b)
# my_function(10,20) # instead of 10,20 we can pass any datatype
# my_function([1,2,3,4,5],[(10,20,30,40,60),30])
# my_function("Saili",{"name":"Anurag","age":26})
# my_function(True,False)

# my_function(50,60//3)

# 2. default arguments
# def new_function(a = 30,b = 40):
#     print(a,end = ' ')
#     print(b)
# new_function() # 30 40 
# new_function(60) #60 40
# new_function(50,100) #50 100
# new_function(b = 90) # 30 90

# print(new_function()) # None

# 3. keyword arguments
# new_function(b = "Python",a = "Programming in")

# 4. *args 
# def variable_arguments(*args):
#     print(type(args)) #tuple
#     print(args)
#     for item in args:
#         print(item)
#     # a =args[0]
#     # b=args[-1]
#     a,*b = args
#     print(a)
#     print(b)

# variable_arguments()
# variable_arguments(10)
# variable_arguments(20,30,40)
# variable_arguments([1,2,3,4,5],(100))

#  5 **kwargs
# def variable_keyword_arguments(**kwargs):
    # print(type(kwargs)) # dictionary so we can perform all operations of dictionary
    # username =kwargs.get('course')
    # print(username)
    # print(kwargs)
    # print(kwargs.keys())
# print(variable_keyword_arguments())
# variable_keyword_arguments()
# variable_keyword_arguments(name="Saili")
# variable_keyword_arguments(age=24,course="Python",username="Krishna",password = None)

#  Func as argument 
def func_a():
    print("hi")
# func_a #reference 
# print(func_a) # <function func_a at 0x000001E48C111440>

# func_a() #call
# new_name = func_a # type of new_name is fuction, we can print it ,we can call it
# new_name()

# def fun_b(num):
#     print(num)
#     num() # call
#     new = num
#     new() #call
#     print(new)

# my_fun = func_a
# print(type(my_fun)) #type
# print(my_fun) # reference
# my_fun() # call

# fun_b(func_a())
# fun_b(num = func_a) #pass reference not call

# inner function 
# def outer():
#     def _inner():
#         for i in range(5):
#             print(i)
#     _inner()
#     print(_inner)
# outer()

# returning inner function reference from outer
# returning inner function call from outer
def outer():
 
    def _inner():
        for i in range(5):
            print(i)
        return "something"
 
    _inner() # call
    print(_inner)
 
    # return _inner # returning reference to inner
    return _inner()  # returning call to inner
 
 
value = outer()
print(type(value))
 
# value()