def handling():
    x = [5,8,9,9,4]
    try:
        num = int(input("enter a number: "))
        if num in x:
            print(f"{num} is in the list")
        else:
            print(f"{num} is not in the list")
    except Exception as e:
        print("unexpected error:",e)

def zero_error():
    try:
        num = int(input("enter a number: "))
        x = 5/num
        print(x)
    except ZeroDivisionError:
        print("error: divide by zero impossible")

def value_error():
    try:
        num = int(input("enter a number: "))
        print(num)
    except ValueError:
        print("error: enter valid number.")

def type_error():
    try:
        x = "hii" + "" # here if we give any numbers in string it will be added to before word
        print(x)
    except TypeError:
        print("error: the given value can not be operated")

def index_error(index):
    x = ["kalaimamani"]
    try:
        letter = (x[0])
        print(letter[index])
    except IndexError:
        print("error: index value is wrong") # when the function is calling in the bracket we put a index value of number

def key_error():
     data = {"name": "rubitha",
             "age" : 22}
     try:
         print(data['hobby'])
     except KeyError:
         print("error: the given key is not in the dictionary")


def file_not_found_error():
    try:
        x = open("file.text")
        print("file opened",x)
    except FileNotFoundError:
        print("file can not opened")
    except Exception as y: # here we can use any letters to identify the exception mistake
        print("other issue",y)

def import_error():
    try:
      #  x = import calulated
        print("file imported")
    except ImportError:
        print("can not be imported")
    except Exception as r:
        print("some other issuse",r)

"""try:
    import non_existent_module  # This module does not exist
except ImportError:
    print("Error: The module could not be imported. Please check the module name or install it.")"""

"""import subprocess
import sys

module_name = "numpy"  # Replace with the module you need

try:
    import numpy  # Try importing the module
except ImportError:
    print(f"{module_name} is not installed. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])


    # Try importing again after installation
    try:
        import numpy
        print(f"{module_name} has been successfully installed and imported.")
    except ImportError:
        print(f"Failed to install {module_name}. Please install it manually.")"""
