#list inside list
num = [[1,2,3],[4,5,6],[7,8,9]]         #2d list
for sublist in num:
    for i in sublist:
        print(i)
print(num[1][1])

