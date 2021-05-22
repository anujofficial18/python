#fromkeys
d = dict.fromkeys(('name','age','height'),'unknown')
print(d)
num = dict.fromkeys(range(1,11),'unknown')
print(num)

#getmethod
d = {'name':'anuj','age':'18'}
print(d.get('name'))

if 'name' in d:
    print('ok')
else:
    print('no')
    
#or
if d.get('name'):
    print('present')
else:
    print('not present')

#d.clear()
#print(d)


#d1 = d.copy()
#print(d1)
d1 = d
print(d1.popitem())
print(d)