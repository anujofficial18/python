#ex_with_list_comp
def num_to_str (l):
    return [str(i) for i in l if(type(i) == int or type(i) == float)]
print(num_to_str([True,False,[1,2,3],1,2,1.0]))