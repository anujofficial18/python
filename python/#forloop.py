#forloop
name =  input("enter ur name")
temp  = ""
for i in range (0,len(name)):
    print(f"{name[i]}:{name.count(name[i])}")
    temp += name [i]