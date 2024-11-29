
def find_max(arr):
    if not arr: return None
    max_val = arr[0]
    for elem in arr: 
        if elem>max_val:
            max_val=elem
    return max_val
# print(find_max([])) # None
# print(find_max([1,4,1,2,3,111,112])) # 112

def reverse_array(arr):
    start, end = 0, len(arr) -1
    while start < end:
        arr[start],arr[end]=arr[end], arr[start]
        start+=1
        end-=1
    return arr
# print(reverse_array([1,3,4,5])) # [5, 4, 3, 1]

def find_second_largest(arr):
    if len(arr)<2: return None
    largest = second_largest=float("-inf") # Primitive by value assigned.
    for num in arr: 
        ###  Number line ............ SL, L  *
        if num > second_largest:
            if num < largest:
                second_largest=num
            else: # if num > largest:
                second_largest = largest
                largest = num
    return second_largest, largest
            
# print(find_second_largest([])) # None
# print(find_second_largest([2])) # None
# print(find_second_largest([2,2])) # (2, 2)
# print(find_second_largest([2,3,4,2,1,2,4,5,67,])) # (5, 67)

def find_pair_with_sum(arr,target):
    diff = set()
    pairs=[]
    for num in arr:
        if num in diff:
            pairs.append((num, target-num))
        diff.add(target-num)
    return pairs

print(find_pair_with_sum([1,2,3,4,5,4],8)) 


def find_triplet_with_sum(arr,target):
    diff = set()
    pairs=[]
    for num in arr:
        if num in diff:
            pairs.append((num, target-num))
        diff.add(target-num)
    return pairs

# def rorate_array_by_k(arr,k):
#     return arr[k:] + arr[:k]
# print(rorate_array_by_k([1,2,3,4,5],3))
# [4, 5, 1, 2, 3]
