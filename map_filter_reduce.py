# Map it is function has map(func,iterable) this func gets execute on every element in an iterable
# numbers = [2,4,6,8,10] #iterable

# def square(number):
#     return number*number

# squared_numbers_iterator = map(square,numbers)
# x = list(map(square,numbers))
# print(f"I am x is {x}")
# print(squared_numbers_iterator)
# print(type(squared_numbers_iterator)) # class map 

# while True:
#     print(next(squared_numbers_iterator))

# for i in squared_numbers_iterator:
#     print(i)

# squared_numbers = list(squared_numbers_iterator)
# print(squared_numbers)

# Using lambd with map
# nums = [1, 2, 3, 4]
# doubled = map(lambda x: x * 2, nums)

# print(list(doubled))  # [2, 4, 6, 8]
# # Multiple iterables
# a = [1, 2, 3]
# b = [4, 5, 6]

# result = map(lambda x, y: x + y, a, b)
# print(list(result))  # [5, 7, 9]

# Tak1
# You are given a list of strings representing numbers that may contain leading/trailing spaces.
data = [' 1', '2 ', ' 3 ', '  4', '5  ']
# Write a one-liner using map() that:

# 1 Strips the whitespace,

#2 Converts each string to an integer,

# 3 Then returns a list of squares of those integers.

#  output [1, 4, 9, 16, 25]

# str_strip = list(map(lambda str1: str1.strip(), data))   # Step 1: Strip whitespaces
# str_int = list(map(int, str_strip))                      # Step 2: Convert to int
# sqr = list(map(lambda x: x**2, str_int))                 # Step 3: Square the numbers
# print(sqr)

# list(map(lambda x: x**2, map(int, map(lambda str1: str1.strip(), data))))  # one liner solution
