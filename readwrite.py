file1 = open("log.txt","r")
y=file1.read()
print(y)
file1.close()
file1 = open("log.txt","w")
x="1"
file1.write(x)
file1.close()
