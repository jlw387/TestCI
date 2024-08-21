def add_one(number):
    if not (type(number) is float or type(number) is int):
        raise TypeError("Must enter a number.")
    
    return number + 1

def times_two(number):
    if not (type(number) is float or type(number) is int):
        raise TypeError("Must enter a number.")
    
    return number * 2

def cube(number):
    if not (type(number) is float or type(number) is int):
        raise TypeError("Must enter a number.")
    
    return number ** 3

def zero(number):
    return 0

if __name__ == "__main__":
    print("One plus one is:", add_one(1))
    print("Two times two is:", times_two(2))
    print("Three cubed is:", cube(3))
    print("Four zeroed is:", zero(4))
