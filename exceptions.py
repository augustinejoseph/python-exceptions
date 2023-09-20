# Attempt to divide by zero
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")

# Attempt to convert a string to an integer
try:
    num = int("abc")
except ValueError as e:
    print(f"Caught a ValueError: {e}")

# Attempt to add a string and an integer
try:
    result = "5" + 10
except TypeError as e:
    print(f"Caught a TypeError: {e}")

# Attempt to access an out-of-range index
try:
    my_list = [1, 2, 3]
    value = my_list[4]
except IndexError as e:
    print(f"Caught an IndexError: {e}")

# Attempt to access a non-existent key in a dictionary
try:
    my_dict = {"name": "Alice"}
    value = my_dict["age"]
except KeyError as e:
    print(f"Caught a KeyError: {e}")

# Attempt to open a non-existent file
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Caught a FileNotFoundError: {e}")

# Attempt to write to a special file (IOError)
try:
    with open("/dev/full", "w") as file:
        file.write("This will raise an IOError.")
except IOError as e:
    print(f"Caught an IOError: {e}")

# Attempt to use a variable that does not exist
try:
    print(variable_that_does_not_exist)
except NameError as e:
    print(f"Caught a NameError: {e}")


# Attempt to call a method on an object that does not have that method
class MyClass:
    pass


obj = MyClass()

try:
    obj.my_method()
except AttributeError as e:
    print(f"Caught an AttributeError: {e}")
