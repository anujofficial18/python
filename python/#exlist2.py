#exlist2
def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
words =('abc','def')
print(reverse_elements(words))

#ex4
def odd_even(l):
    odd_num = []
    even_num = []
    for i in l:
        if i%2==0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output = [odd_num,even_num]
    return output
nums = [1,2,3,4,5,6,7,8,9]
print(odd_even(nums))

#ex5
def sep_num(l1,l2):
    seperate_num = []
    for i in l1:
        if i in l2:
            seperate_num.append(i)
    return seperate_num
print(sep_num([1,2,3,4],[1,2,5,6]))
