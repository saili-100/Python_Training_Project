# List 
#Syntax = []
my_list = []
print(type(my_list))

# List can store any data type
new_list = [10,20.3,8+5j,True,"Python",[10,20,30,-6],(1,2,3),{9,8,7},20.3]
print(new_list)
#  List is Mutuable
lst = [2,3]
lst[0] = 10 
print(lst)
# List is slower than tuple 
# Allows duplicate values :on line no 7 
# List is ordered 
# sort append extend 
lst.sort() 
# Checking in built methods in list dir(list)
lst.append(10)
lst.extend(["Saili","Nikita"])
print(lst)

