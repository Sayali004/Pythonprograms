f = open("file.txt", "r")  
content = f.read()
print(content)
f.close()

f2 = open("file2.txt", "r")  
content2 = f2.readline()
print(content2)
f2.close()

f3 = open("file3.txt", "r")  
content3 = f3.readlines()
print(content3)
f3.close()

