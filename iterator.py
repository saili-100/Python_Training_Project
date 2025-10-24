# Iterator
 
it = iter([10, 20, 30, 40])
print(it) #<list_iterator object at 0x0000026A568EABC0>
print(type(it)) # <class 'list_iterator'>
 
it2 = iter({1, 2, 3, 4, 5})
print(type(it2)) # <class 'set_iterator'>
 
it3 = iter((1, 2, 3, 4, 5))
print(type(it3)) #<class 'tuple_iterator'>
 
 