def what_are_the_vars(*args, **kwargs):
    # Create an instance of ObjectC
    obj = ObjectC()
    
    # Set the attributes for the instance using *args
    for i, arg in enumerate(args):
        setattr(obj, f'var_{i}', arg)
    
    # Set the attributes for the instance using **kwargs
    for key, value in kwargs.items():
        setattr(obj, key, value)
    
    return obj


class ObjectC(object):
    def __init__(self):
        # Initialize the object with no attributes
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    
    # Print the attributes of the object
    for attr in dir(obj):
        if attr[0] != '_':  # Skip private attributes (those starting with '_')
            value = getattr(obj, attr)
            print(f"{attr}: {value}")
    
    print("end")


if __name__ == "__main__":
    # Example calls based on the prompt
    obj = what_are_the_vars(7)
    doom_printer(obj)
    
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    
    obj = what_are_the_vars()
    doom_printer(obj)
    
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
