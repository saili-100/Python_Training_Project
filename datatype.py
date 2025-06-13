# Datat type
# String Integer Float Boolean Complex List Tuple Set Dictionary None 
a = None #Nothing 
# Checking data type type syantx type(Variable name)
# print(type(a))

# range
# x = range(2,6) 
# print(x)
# print(type(x))
# for i in x:
#     print(i)

# String
name = "Saili"

# Integer 
num = 500

#Float 
num1 = 10.6

# Complex
num2 = 10-3j

# List 
my_list = ["Saili",10,20.6,9+3j,True,(1,2,3)]

# Tuple
my_tuple = ("apple","orange","mango")

# Set
my_set = {10,20,30,40,(9,8,7,-6)}

# Dictionary
my_dict = {1:"Saili",2:"Pooja",3:"Suraj"}

# Boolean 
my_boolean = True 

result = [name,num,num1,num2,my_list,my_tuple,my_set,my_dict,my_boolean]

data_type=["string","integer","float","complex","list","tuple","set","dictionary","boolean"]

for i in range(len(result)):
    print(f"{result[i]} I am {data_type[i]} ")

# print(f"{name} I am string")
# print(f"{num} I am integer")
# print(f"{num1} I am float")
# print(f"{num2} I am complex")
# print(f"{my_list} I am list")
# print(f"{my_tuple} I am tuple")
# print(f"{my_set} I am set")
# print(f"{my_dict} I am dictionary")
# print(f"{my_boolean} I am boolean")