# Append mode 
file_obj = open(file="write.txt", mode="a")
# file_obj.write("This is a third line.\n")
# file_obj.write("This is fourth line.\n")
# file_obj.write("This is a fifth line.\n")
# file_obj.close()
# file_obj = open(file="write.txt", mode="r")
# for line in file_obj:
#     print(line)
# print(file_obj.readline()) #why spaces ?
# print(file_obj.readline())
# print(file_obj.readlines())
# file_obj.close()


# different modes
# r - read
# w - write (overwrites the file)
# a - append (adds to the end of the file)
# r+ - read and write (does not overwrite the file)
# w+ - write and read (overwrites the file)
# a+ - append and read (adds to the end of the file)
# rb - read binary
# wb - write binary (overwrites the file)
# ab - append binary (adds to the end of the file)

# using with statement
with open(file="notes.txt", mode="r") as file_obj:
    contents = file_obj.read()
    print(contents)
 
print(type(contents))
 
file_obj.readline()
 
# context manager
 
# with <context> as <variable>:
    # code block
    # pass
 
# context manager with multiple files
 
# with open(file="notes.txt", mode="r") as file_obj1, open(file="notes2.txt", mode="w") as file_obj2:
#     contents = file_obj1.read()
#     file_obj2.write(contents)
 
print("Files processed successfully.")