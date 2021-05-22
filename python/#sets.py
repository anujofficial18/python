#sets
s = {1,2,3}
print(s)
l = [1,2,3,4,5,6,6,7,7,8,8,4]
#remove duplicates
s2 = set(l) #to createlist ---> s2 = list(set(l))
print(s2)
#to add values
s.add(4)
print(s)
#to remove
s.remove(3)
print(s)
#to clear
#s.clear()
s1 = s.copy()
print(s1)