# # Generator
# def normal_function():
#     for i in range(5):
#         print(i)
 
# normal_function()
# print(type(normal_function))
 
# def my_generator():
#     # body
#     for i in range(5):
#         yield i
 
# my_gen = my_generator()# created object
# print(my_gen) # generator objct
# print(type(my_gen)) # class generator
 
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# # print(next(my_gen))
# # print(next(my_gen))
# # print(next(my_gen))

# def generator_function():
#     for x in range(10**15):
#         yield x

# my_gen = generator_function()
# print(my_gen)
# # print(next(my_gen))

# while True:
#     print(next(my_gen))

# def gen_fun():
#     for x in range(11):
#         yield x
# my_gen =gen_fun()
# # # print(next(my_gen))
# # # while True:
# # #     print(next(my_gen))
# for i in my_gen:
#     print(next(my_gen))
#     # print(i)

# d = (x for x in range(10))
# print(d) # generator object 
# print(type(d)) # generator
# print(next(d))
# to get what is present inside it we use next(generator object i.e d)
# while True:
#     print(next(d))
# for i in d:
    # print(next(d))
    # print(i)
    # print(next(i)) #wrong

def gen_fun():
    for x in range(11):
        yield x 
my_gen = gen_fun()
for _ in my_gen:
    print(next(my_gen))
    
    

