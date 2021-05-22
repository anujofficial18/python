#dictionary_comprehension
square = {1:2,2:4,3:9}
square1 = {f"square of {num} is":num**2 for num in range (1,11)}
for k,v in square1.items():
    print(f"{k}:{v}")

string = "jdfhusvh"
word_count = {char:string.count(char) for char in string}
print(word_count)

#if_else_with_dict_comprehension
odd_even = {i:('even'if i%2 == 0 else 'odd')for i in range(1,11)}
print(odd_even)