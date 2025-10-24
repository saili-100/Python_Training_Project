## opening a file
# reading a file read() readable() readline() readlines()
# writing a file
# updating a file
 
# relative
# notes.txt
# /Users/anurag/Projects/Occupyed/python_project/notes.txt
# file_obj = open(file="/Users/anurag/Projects/Occupyed/python_project/notes.txt", mode="rb")
file_obj = open(file = "notes.txt",mode="r")
# print(file_obj)
# print(dir(file_obj))# methods we use with files
# print(type(file_obj))
 
# contents = file_obj.read()
# print(contents)
# print(type(contents))
 
# print(file_obj.readable())
 
line = file_obj.readline() # reads first line like generator on demand . doubt why space in output ?
print(line.strip())
line = file_obj.readline()
print(line)
line = file_obj.readline()
print(line)
# line = file_obj.readline()
# print(line)
# line = file_obj.readline()
# print(line)
 
# lines = file_obj.readlines() # returns list , returns remaining lines after readline() []dict
# print(lines)
file_obj.close()
# line = file_obj.readline()
# print(line)


#  Can we use python file too and modify it?