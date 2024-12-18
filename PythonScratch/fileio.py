s = "Hello its Tuesday!!!"
# #Writing File
# with open("text.txt","w") as f:
#     f.write(s)

#method 2
# fp = open("text.txt","w")
# fp.write(s)
# fp.close()

#Reading a file
# with open("text.txt","r") as f:
#     s1 = f.read()
#     print(s1)

# f = open("demo.txt", "r")
# w = f.read()
# print(w)
# f.close()


# with open("text.txt","w") as f:
#      f.write("Welcome to school")

with open("text.txt","a") as f:
    f.write(s)
    f.write("Welcome to school...")