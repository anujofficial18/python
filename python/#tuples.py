#tuples
#tuples data structure
#tuples can store any data types
#imutables  (noappend,no pop, no remove after creating)
#tuples are faster than list
#methods (count,index,len fun, slicing[:2])
ex = ('one','two','three')
print(ex[:2])

#1.looping in tuples
#2.tuple with one element
#3.tuple without parenthesis
#4.tuple unpacking
#5.list inside tuple
#6.some func u can use with tuple

#1
mixed = (1,2,3,4.0)
for i in mixed:
    print(i)

#2
num = (1,)    #tuble value k bas  '1,' pr hi tuple hota h  
words = ('one',)
print(type(num))
print(type(words))

#3
names = 'anuj','mayank','didi'     #',' ke bina bhi tuple ho skta h
print(type(names))

#4
members = ('anuj','mayank','rohit')
member1,member2,member3 = (members)
print(member1)

#5
#name = ('apple','melon',['mango'])
#name[1].pop()
#name[1].append("we made it")
#print(name)

#6
#min(), max, sum
print(max(mixed))
print(sum(mixed))
