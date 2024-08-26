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

def identity(number):
    return number

if __name__ == "__main__":
    # Woah comment
    print("Starting up program...\n")

    print("One plus one is:  ", add_one(1))
    print("Two times two is: ", times_two(2))
    print("Three cubed is:  ", cube(3))
    print("Four zeroed is:   ", zero(4))
    print("Five is:          ", identity(5))
    
    print("\nThank you for running this program!")

<<<<<<< HEAD
    # Comment added to test feature branch workflow
    
=======
    
>>>>>>> development
