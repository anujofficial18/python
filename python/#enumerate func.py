#enumerate func
names = ['fdsdf','sjbfkb','bhsachb']
pos = 0
for name in names:
    print(f"{pos}-----{name}")
    pos += 1

#with enumerate
for pos , name in enumerate(names):
    print(f"{pos}-----{name}")