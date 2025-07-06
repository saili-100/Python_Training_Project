# Function
# define fun
# calling function
# return 
# returning multiple values 
# Function as an object (Functions are first class objects.)
# Aim to learn decorator

def get_name():
    return "My name is Saili",10,True
name = get_name() # store data in form of tuple
print(name,type(name))
# var1,var2,var3 = get_name()
# var1,*var2 = get_name()
# print(var1,type(var1))
# print(var2,type(var2))
# print(var3,type(var3))

# IMP 
# return value can be int,float,str,list,tuple,set ,dictionary [] () {} {}
# stmt after return does not execute case--> if return in different block that will get execute

def function_a():
    pass
def function_b():
    return 
def function_c():
    return None 
a= function_a()
b = function_b()
c =function_c()
print(a)
print(b)
print(c)

# As return value is tuple in line no 6 we can perform all operations related to tuple. 
# like indexing, iterate,unpacking
print(name[1])

for i in name:
    print(i)

p,q,r = name #tuple unpacking 
print(p,q,r)

def function_e():
    return {"Key":"value"}
function_e()
print(function_e) #<function function_e at 0x0000022C8FE9C220> gives memory location of function where it is stored in ram 
var = function_e # rename function 
print(var)
# line 43 ,45 points to same memory location in ram where function is stored
new_name = get_name # refeence
print(new_name)
ten = get_name
print(ten)
print(new_name())
print(ten())

# Function is nothing but new datatype. It behave same as other other data type . We can print function,rename func and id()
print(type(new_name))
print(type(get_name))
print(id(new_name),id(get_name))

# function can be rename , it has id ,type()
def f():
    pass 
a = f #rename 
id(f)
type(f)
id(a)
type(a)
a()

