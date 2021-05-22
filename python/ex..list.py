#exlist
#num = [1,2,3,4,5,6]
def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
number = list(range(1,11))
print(square_list(number))      

#ex2

def reverse_list(l):
    l.reverse()
    return l     #or   return l[::-1]
numbers = [1,2,3,4]
print(reverse_list(numbers))

def rev_list(l):
    r_list = [ ]
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list
number = [1,2,3,4]
print(rev_list(number)