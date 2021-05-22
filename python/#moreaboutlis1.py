#moreaboutlist
#number = list(range(1,11))
#popped_item = number.pop()
#print(number)
#print(number.index(1))
number = [1,2,3,4,5,6,7]
def negative_list(l):
    negative = []
    for i in  l:
        negative.append(-i)
    return negative
print(negative_list(number))