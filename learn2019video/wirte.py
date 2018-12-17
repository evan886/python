f=open("hey.txt","w")
f.write("hello")
f.close()

f=open("hey.txt","r")
content = f.read()
print(content)
f.close()
