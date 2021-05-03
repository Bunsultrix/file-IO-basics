 # file IO basics

# 'r' - open file for read {default}
# 'w' - open file for write
# 'x' - creat file if not exists
# 't' - text mode {default}
# 'b' - binary mode
# '+' - read and write

#FILE READIND

#f = open("nitish.txt")  # {this is how we open the file [it should be in txt format]}
# print(f.readline())   #{this will read file line by line }
# print(f.readlines())   #{this will print file in list}
#
# content = f.read()  #{this how we read the file }
# print(content)    #{this is how we print all the content in the file }
# # f.close()    #{this is how we close the file}

#FILE WRITE
# f = open("nitish2.txt",'w') #{this how we make new file aor over write on old file}
# f.write('nitish is good boy , this file will run with file IO basics')
#f.close()

#FILE WRITTING AND READING
f = open("nitish.txt" ,'a')
a= f.write('\n this file will run with file IO basics ')
print (a)
