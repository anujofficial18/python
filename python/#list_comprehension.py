#list_comprehension
squares = []
for i in range (1,11):
    squares.append(i**2)
print(squares)
squares2 = [i**2 for i in range(1,11)]
print(squares2)

negative= []
for i in range(1,11):
    negative.append(-i)
print(negative)
negative1 = [-i for i in range(1,11)]
print(negative1)

names = ['anuj', 'mayank','rohit']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)
new_list1 = [name[0]for name in names]
print(new_list1)


#list_comprehension_with_if_statement
numbers = list(range(1,11))
nums = []
for i in numbers:
    if i%2 == 0:
        nums.append(i)
print(nums)

#now with list comprehension
even_nums = [i for i in numbers if i%2 == 0]
print(even_nums)
even_nums2 = [i for i in range(1,21) if i%2 == 0]
print(even_nums2)
odd_nums = [i for i in range(1,11) if i%2 != 0]
print(odd_nums)

#list_comprehension_with_if_else_statement
num = [1,2,3,4,5,6,7,8,9,0]
new_list2 = []
for i in nums:
    if i%2 == 0:
        new_list2.append(i*2)
    else:
        new_list2.append(-i)
print(new_list2)

#now with list comprehension
new_list3 = [i*2 if (i%2 == 0) else -i for i in num]
print(new_list3)

#list_comprehension_with_nested_list
example = [[1,2,3],[1,2,3],[1,2,3]]
nested_comp = [[i for i in range(1,4) ]for j in range(3) ]
print(example)