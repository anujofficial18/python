#more_about_sets
s = {'a','b','c'}
if 'a' in s:
    print("present")
else :
    print("not present")

for item in s:
    print(item)

s1 = {1,2,3,4}
s2 = {3,4,5,6}
union_set = s1 | s2   #for union
print(union_set)
#for intersection
print(s1 & s2)