# Writing a file  'writable', 'write', 'write_through', 'writelines'
file_obj = open(file="write.txt",mode="w")
# print(file_obj.read())
# print(dir(file_obj))

file_obj.write("This is first line\n")
file_obj.write("This is second line\n")

# if file_obj.writable():
#     file_obj.write("This is a third line.\n")

# file_obj.close()

# file_obj = open(file="write.txt",mode="r")
# print(file_obj.readline())
# print(file_obj.readline())
# print(file_obj.readlines())
# lines = ["This is a new line.\n", "This is another line.\n",]   
# file_obj.writelines(lines)
# iterating over a file
# file_obj = open(file="notes.txt", mode="r") 
# for line in file_obj:
#     print(line.strip())

# seek method 