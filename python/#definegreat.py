#definegreat
def greater(a,b,c):
    if a > b and a>c:
        return a
    elif b > c and b>c:
        return b
    else:
        return c
num1 =int(input("enter"))       
num2 =int(input("enter")) 
num3 =int(input("enter"))
bigger = greater(num1,num2,num3)
print(f"{bigger} is greater")