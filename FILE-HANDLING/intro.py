import os
# f= open("test.txt", "r", encoding="utf-8")
# lines= f.readlines()
# print(lines[2])
# f.close()

# f = open("missing.txt","w", encoding="utf-8")
# f.write("Valentine is a big boy")
# f.close()

# cerati
# f = open("My_Morning.txt", "x", encoding="utf-8")
# f.write("1. I prayed this morning.\n2. I had my bath.\n3. I cleaned my shoes.\n4. I used my phone.\n5. I went to class.")
# f.close()

# # CORRECTION
# # We create a List of Task
# tasks = []



# Shortcut to write the open file code
# with open("test.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# Now let's use the try & except keyword.
# try:
#     with open("life.txt", "r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     # print("File not found, please check the file name and try again.")
#     with open("life.txt", "w", encoding="utf-8") as f:
#         f.write("This File was created because it was missing.\n")



# READ AN IMAGE FILE
#with open("image.png", "rb")
# print(f.read()) 

# COPY AND PASTE IMAGE
# with open("image.png", "rb")

# def second_item(x):
#     try:
#         return x[1]
#     except IndexError:
#         return "List is too short."
#     except TypeError:
#         return "Input must be a list"
#     else:
#         return "Second item is", x[1]
# print(second_item(1))


# CLASS WORK 18 DECEMBER 2025
#assignment: usernames should not have number, and visitors should not be allowed till after 5 mins
# visitors_name = []


# with open("visitors.txt", "x", encoding="utf-8") as f:
#     f.write("")

# user_name = input("Enter Visitor's name: ")


# MAKING USE OF THE IMPORT OS FOR PYTHON TO INTERACT WITH MY COMPUTER LOCALLY FOR BASIC PYTHON FILE DETECTION.

# This is a relative file path.
file_path = "life.txt"

# This is an absolute file path.
# file_path = "C:/Users/USER/Desktop/NCAIR/PYTHON/Python Advanced/REGEX"

# if os.path.exists(file_path):
#     print(f"The file is located at '{file_path}' ")
#     if os.path.isfile(file_path):
#         print("This is a file")
#     elif os.path.isdir(file_path):
#         print("This is a directory.")
# else:
#     print("File path does not exist.") 

# OLD WAY IN PYTHON TO READ A FILE
# f = open("life.txt", "r")
# print(f.read())
# print(f.readlines())

with open("life.txt", "w") as f:
    f.write("I am a King! \n")





