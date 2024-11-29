l = [1, 2, 3, 4, 5, 6, 8, 9, 10]
def find_missing(arr):
    init =1
    for i in l :
        if i !=init:
            return init
        init=init+1
        
print(find_missing(l))
