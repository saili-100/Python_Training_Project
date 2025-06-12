# In casting we can change one datatype to another datatype 
# for eg
num = 10
print(type(num))
res=float(num)
print(type(res))

my_string = "50"
print(type(my_string))
result = int(my_string)
print(type(result))

# fstring
# We format the string 
# for eg
for i in range(10):
    str = f"{i} earlier this data type was string but after casting we changed to integer"
    print(str) 