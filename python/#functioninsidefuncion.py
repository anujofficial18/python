#functioninsidefuncion
def greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)
print(greatest(10,20,30))