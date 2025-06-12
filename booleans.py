# Booleans
# True False
# eg 
print(5>2)
print(5==6)
a=5
b=6
if a!=b:
    print(True)
else:
    print(False)

d = True
c = False 
if d:
    print("Yes1")
if c:
    print("Yes")

print(bool({})) #False
print(bool({1:"Apple"})) # bool(any data type)
print(bool(None))
print(bool("")) 

def fun():
    return True
# a=fun()
if fun():
    print("Yes")
else:
    print("No")