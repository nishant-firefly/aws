def dec(func):
    def wrapper(*args, **kwargs):
        print("Before Called")
        print(args)
        resp=func(*args,**kwargs)
        print("After Called")

    return wrapper
@dec
def normal_func(i,j):
    print("HI")
normal_func(1,2)

def param_dec(n):
    def dec(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"= Call {i + 1} of {n} =")
                resp = func(*args, **kwargs)
            return resp  # Return the result of the last call
        return wrapper
    return dec

@param_dec(3)
def another_func(i, j):
    print(f"Processing {i} and {j}")
    return i * j  # Example return value

result = another_func(3, 4)
print(f"Result: {result}")

