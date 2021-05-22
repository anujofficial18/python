#min and max fun
numbers = [1,50,5]
print(min(numbers))
print(max(numbers))

def gretest_number(l):
    return max(l) - min(l)
print(gretest_number(numbers))



#ex6
def sublist_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
mixed = [1,2,3,[4,5,6],[6,7,8]]
print(sublist_count(mixed)) 