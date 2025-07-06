# # # Tuple
# # # Syntax ()
# # my_tuple = (10,20,30,40,50)
# # # Immutable 
# # print(my_tuple[0])
# # # my_tuple[0] = -2 # We can't modify tuple so error on this line hence it is immutable.

# # # ordered
# # # faster than list 
# # import timeit 
# # setup='''
# # Data_list = list(range(80000000))
# # DataTuple = tuple(Data_list)'''
# # tuple_time = timeit.timeit("for i in DataTuple:pass",setup=setup,number=1)
# # list_time = timeit.timeit("for i in Data_list :pass",setup=setup,number=1)

# # print(list_time,"list time")
# # print(tuple_time,"tuple time")
# # # tuple with single element put comma 
# # # eg tup=(11,)
# # # only 2 methods count index

# import time
 
# data_list = list(range(800000000))
# data_tuple = tuple(data_list)
 
# start = time.time()
# for i in data_list:
#     pass
# list_time = time.time() - start
 
# start = time.time()
# for i in data_tuple:
#     pass
# tuple_time = time.time() - start
 
# print(f"List iteration time: {list_time:.5f} seconds")
# print(f"Tuple iteration time: {tuple_time:.5f} seconds")
 
# tup=(20,)
# print(type(tup))

t = (1,2,3,4,5)  
# x,*y = t
# x,y,*z = t
x,*y,z = t
print(x,type(x))
print(y,type(y))
print(z,type(z))
