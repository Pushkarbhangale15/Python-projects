# with open("my_file.txt") as file:
#     contents=file.read()
#     print(contents)
#     file.close()

with open("my_file.txt","+a") as file:
    file.write("How are You?")
    contents=file.read()
    print(contents)