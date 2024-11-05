def list_comp(arr, condition=None, function=None):
    #List Comprehension Wrapper
    def evaluate_each(func, index):
        return func(index) if func  else index
    return [evaluate_each(function, i) for i in arr if condition] if  condition else [evaluate_each(function, i) for i in arr]

print("range in Python 3 returns a range object that generates numbers on demand, without creating an entire list in memory just like in xrange in python2")
print(f"range(starting_with_zero_to_number_minus_1) E.g range(10) :{list_comp(range(10))}") # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(f"range(starting_with_index, end_index_minus_1) E.g. range(1,10) :{list_comp(range(1,10))}") # [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(f"range(starting_with_index, end_index_minus_1, with_duration_step) E.g. range(1,10,3) :{list_comp(range(1,10,3))}") # [1,4,7] 
print(f"range(1,11,3) :{list_comp(range(1,11,3))}") # [1,4,7,10] 
print(f"range(0,10,3) :{list_comp(range(0,10,3))}") # [0,3 6,9] 
print(f"range(0,13,3) :{list_comp(range(0,13,3))}") # [0,3 6,9,12] 
