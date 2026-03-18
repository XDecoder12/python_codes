'''
print("Hello", "World", sep="-")

print("Line 1", end=" ")
print("Line 2")

with open("output.txt", "w") as f:
    print("This will be written to a file.", file=f)

import time
print("Processing...", end="", flush=True)
time.sleep(15)
print("Done!")

name = "Alice"
age = 20
print(f"Name: {name}, Age: {age}")

print("Name: {}, Age: {}".format("Bob", 25))
print("Hello" + " " + "Python")


name = input("Enter your name: ")
print("Hello,", name)

age_str = input("Enter your age: ")
age_int = int(age_str)
print("You will be", age_int + 1, "next year.")

temperature = float(input("Enter teh temperature in Celcius: "))
print("Temperature in Fahrenheit: ", (temperature * 9/5) + 32)

name = input("What's your name? ")
print("Hello,", name, "!")

x, y = map(int, input("Enter two numbers separated by space: ").split())
print("First number: ", x)
print("Second number: ", y)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Addition ",num1+num2)
print("Substraction ",num1-num2)
print("Multiplication ", num1*num2)
print("Division ", num1/num2)
print("Modulus ",num1%num2)
print("Floor Division ",num1//num2)
print("Exponent",num1**num2)


x = "This is global scope/space"
def outer_func():
    x = "This is enclosing scope/space"
    print(x)
    def inner_func():
        x = "This is local scope/space"
        print(x)
    inner_func()
outer_func()


z=9
y=14
print(~y)
string = 'hii how are you'
if 'hii' in string:
    print(True)
else:
    print(False)
'''


#Match Expression: it is the value........

#Case Pattern: it defines each case against the expression

#OR Operator(|): used to combine multiple patterns in a single case

#if condition(guard): it is used as a clause to guard a case

#underscore(wildcard/default): used for default cases

'''
count = 1
while count <= 5:
    print(f"Const is: {count}")
    count += 1

user_string = " "
while user_string.lower() != "quit":
    user_string = input("Enter  something (or 'quit' to exit): ")
    if user_string.lower() != "quit":
        print(f"You entered: {user_string}")
print("Exiting the program.")

i = 0
while i < 4:
    print(f"Inside loop: {i}")
    i += 1
    break
else:
    print("Loop finished successfully.")
'''

#do-while of python

'''
def process_command(command):
    match command:
        case "start":
            print("Starting the process...")
        case "stop":
            print("Stopping the process...")
        case "pause" | "resume":
            print(f"Executing {command} command.")
        case "status" if some_condition:
            print("Checking status...")
        case _:
            print(f"Unknown command: {command}")

process_command("start")
process_command("pause")
process_command("unknown")


def my_function():
    pass # This function does nothing for now

class MyClass:
    pass # This class is empty for now

for i in range(3):
    if i % 2 == 0:
        print(f"{i} is even.")
    else:
        pass # Do nothing if the number is odd

for i in range(5):
    if i == 2:
        continue # Skip printing when i is 2
    print(i)

for i in range(5):
    if i == 3:
        break # Exit the loop when i is 3
    print(i)
print("Loop finished.")



import array as arr

# Create an array of signed integer
my_int_array = arr.array("i", [1, 2, 3, 4, 5])
print(f"Integar array: {my_int_array}")

# Create an array of double-precision floats
my_float_array = arr.array("d", [1.1, 2.2, 3.3])
print(f"Float array: {my_float_array}")

# Create an empty array
empty_array = arr.array('i')
print(f"Empty array: {empty_array}")

print(f"First element: {my_int_array[0]}")
print(f"Last element: {my_int_array[-1]}")

my_int_array.append(6)
my_int_array.insert(1, 10)
my_int_array.extend([7, 8])
print(f"Array after adding elements: {my_int_array}")

removed_element = my_int_array.pop(2)
my_int_array.remove(5)
print(f"Array after removing elements: {my_int_array}")
removed_element = my_int_array.pop(4)
# my_int_array.remove(5)
print(f"Array after removing elements: {my_int_array}")
print("Length:", len(my_int_array))
print("Index:", my_int_array.index(10))
my_int_array.reverse()
print(f"Reversed array: {my_int_array}")
'''

#len(array): Returns the number of elements in the array.

#index(x): Returns the address of the first occurrence of x.

#reverse(): Reverses the order of elements in the array.


# Data Structures in Python: Python programing provides data structures for storing and arranging data which are easily accessible and modifiable, these are called in python as collection data structures. The commonly used builtin collections are list, tuples, dictionaries and sets.

# LIST: This is a collection data structure that allows to store multiple items of different data types in a single variable, unlike classical arrays of C/C++ python lists are arrays that stores heterogeneus data types
# We create a list by placing elements in a square bracket seperated by comma (just like arrays)
# They are ordered, they are mutable and allow duplication
# The elements in the list are accessed through the index and the index of the 1st element is zero.
# In python we have negative indexing so the last element can be accessed by -1.
# To access a certain range of elements in the list we use the colon operator ":" which is known as slicing.
# In python everything is a class, lists is also a classe having various methods and these methods are used to manipulate the lists.
# Append: add an element at the end of the list
# Insert:
# Remove: this is used to remove any specified element form the list
# len: this is a built in length function that is used to find the number of elements in the lists
# pop: removes the item at a given index
# reverse: it reverses the items of the list

# TUPLE: it is also a collection data structure in python similar to list with one primary difference that it is immutable once it is created, a touple is created by using ()
# They are ordered, they are immutable, they allow repeated
# They can be accessed by the index which starts from 0
# Len method is used to find the length of the tuple.

# DICTIONARY{}: it is also a collection data structur in python which is having a key value pair
# The keys of the dictionary must be immutable similar to that of tuple
# accessing the dictionary can be done by placing the key inside the square bracket
# we use the len function to find the length of the dictionary
# get: that returns the value of the specified key
# update: changes or adds to the dictionary item

# SET: it is also a built in data structure in python which is an unordered collection of unique elements
# it is denoted by elements inside the {} , seperated by comma
# it can have different data tyeps like int, float, touple, strings, etc,.
# it can't have mutable elements like lists or dictionaries
# we can denote an empty set using the set function [empty_set = set()]
# we have various methods to operate on the sets
# add method: add() is used to add an item to the set
# update(): is used to update the set with other collection types
# len(): is used to find the length of the set
# max(): returns the largest element in the set
# min(): returns the samllest element in the set
# sorted(): returns a new list of sorted elements from the set
# sum(): returns the sum of all the elements of the set
# Operations on the set: Union(A|B or A.union(B)) , Intersection(A&B or A.intersection(B)), Difference(A-B or A.difference(B)), Symmetric-Difference(A^B or A.symmetric_difference(B)).
# The other methods of sets are : isdisjoint(), issubset(), remove(x), 

'''
numbers = [1,2,3,4,5]
print(numbers)

fruits = ["apple", "orange", "grapes"]
print(fruits)

mixed_list = [10, "text", False, 35.34]
print(mixed_list)

colors = ["red", "green", "blue"]
print(colors[0])
print(colors[1])
print(colors[-2])
print(colors[-1])

my_list = ["book", "pen"]
my_list.append("laptop")
my_list[0] = "notebook"
print(my_list)

more_items = ["chair", "table"]
my_list.extend(more_items)
print(my_list)

my_list.insert(3, "pencil")
print(my_list)

shopping_list = ["bread", "butter", "milk", "panner"]
shopping_list.remove("butter")
print(shopping_list)

popped_item = shopping_list.pop(1)
print(popped_item)
print(shopping_list)

shopping_list.clear()
print(shopping_list)

vowels = ["a", "e", "i", "o", "u"]

subset = vowels[2:4]
print(subset)

start_slice = vowels[:2]
print(start_slice)

end_slice = vowels[3:]
print(end_slice)

print(f"Length of numbers: {len(numbers)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"First element: {numbers[0]}")
print(f"Subset of numbers: {numbers[1:3]}")

data = [4, 3, 6, 8, 2, 7]

data.sort()
print(f"Sorted data: {data}")
data.reverse()
print(f"Reversed data: {data}")

unsorted_data = [4, 5, 54, 3, 7, 35]
sorted_data = sorted(unsorted_data)
print(f"New sorted data list: {sorted_data}, Original data list: {unsorted_data}")

empty_tuple = ()
my_tuple = ("grapes", 32, False, 4.5, 32)
print(my_tuple[2])
single_item_tuple =  ("pen")

tuple_from_list = tuple(my_list)
print(tuple_from_list)

my_tuple = (2, 4, 1, 6, 9, 7, 1, 1)
count_of_two = my_tuple.count(1)

tuple_eg = ("apple", "grapes", "lichi", "guava")
print(tuple_eg.index("guava"))

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

t1 = (1, 3, 6)
t2 = (4, 7, 2)
print(t1 + t2)

t = ("Text",)
print(t * 3)

t = ("guava", "lichi", "orange")
print("apple" in t)
print("orange" in t)

t = (2, 3, 9, 5, 6)

print(len(t))
print(t.count(9))
print(t.index(5))


my_dict = {"brand": ["Toyata", "Maruti", "Audi"], "model": ["hilux", "dzire", "Q7"], "year": [2022, 2025, 2024]}
another_dict = dict(name="Tom", age=22)

print(my_dict["model"])
print(another_dict.get("city", "Unknown"))

my_dict["color"] = "black"
my_dict["year"] = 2021
del my_dict["year"]
removed_value = my_dict.pop("model")
last_item = my_dict.popitem()

for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(f"{key}: {value}")

my_dict = {"a" : 1, "b" : 2}
my_dict.clear()
print(my_dict)

original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()
print(copied_dict)

keys = ["banana", "orange"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

my_dict = {"name": ["Ramu"], "age": [25], "city": ["Hyderabad"]}
name = my_dict.get("name")
city = my_dict.get("city", "Unknown")
print(name)
print(city)




# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}
print(f"Set created with curly braces: {my_set}")

# Creating a set from a list (duplicates are automatically removed)
list_data = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list_data)
print(f"Set created from a list: {set_from_list}")

# Creating a set from a string (each character becomes an element)
string_data = "hello"
set_from_string = set(string_data)
print(f"Set created from a string: {set_from_string}")

my_set = {1, 2, 3}

# Adding a single element
my_set.add(4)
print(f"After adding 4: {my_set}")

# Adding multiple elements using update()
my_set.update([5, 6])
print(f"After adding 5 and 6: {my_set}")

# Removing an element
my_set.remove(3) # Raises KeyError if element element not found
print(f"After removing 3: {my_set}")

# Discarding an element (does not raise error if element not found)
my_set.discard(10)
print(f"After discarding 10: {my_set}")

# Removing a random element
removed_element = my_set.pop()
print(f"Removed element using pop(): {removed_element}, remaining set: {my_set}")

# Clearing all elements
my_set.clear()
print(f"After clearing the set: {my_set}")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (elements in either set)
union_set = set_a.union(set_b)
print(f"Union of A and B: {union_set}")
# Alternative using | operator
union_set_operator = set_a | set_b
print(f"Union using | operator: {union_set_operator}")

# Intersection (elements common to both sets)
intersection_set = set_a.intersection(set_b)
print(f"Intersection of A and B: {intersection_set}")

# Alternative using & operator
intersection_set_operator = set_a & set_b
print(f"Intersection using & operator: {intersection_set_operator}")

# Difference (elements in set_a but not in set_b)
difference_set = set_a.difference(set_b)
print(f"Diffrence (A - B): {difference_set}")
# Alternative_ using - operator
difference_set_operator = set_a - set_b
print(f"Difference using - operator: {difference_set_operator}")

# Symmetric Difference (elements in either set, but not in both)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"Symmetric difference of A and B: {symmetric_difference_set}")
# Alternative using ^ operator
symmetric_difference_set_operator = set_a^set_b
print(f"Symmetric Difference of A and B using ^ operator:{symmetric_difference_set_operator}")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {6, 7}

#issubset()
print(f"Is set_x a subset of set_y?: {set_x.issubset(set_y)}")

# issuperset()
print(f"Is set_y a superset of set_x?: {set_y.issuperset(set_x)}")

# isdisjoint()
print(f"Are set_x and set_z disjoint?: {set_x.isdisjoint(set_z)}")




# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}
print(f"Set created with curly braces: {my_set}")

# Creating a set from a list (duplicates are automatically removed)
list_data = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list_data)
print(f"Set created from a list: {set_from_list}")

# Creating a set from a string (each character becomes an element)
string_data = "hello"
set_from_string = set(string_data)
print(f"Set created from a string: {set_from_string}")

my_set = {1, 2, 3}

# Adding a single element
my_set.add(4)
print(f"After adding 4: {my_set}")

# Adding multiple elements using update()
my_set.update([5, 6])
print(f"After adding 5 and 6: {my_set}")

# Removing an element
my_set.remove(3) # Raises KeyError if element element not found
print(f"After removing 3: {my_set}")

# Discarding an element (does not raise error if element not found)
my_set.discard(10)
print(f"After discarding 10: {my_set}")

# Removing a random element
removed_element = my_set.pop()
print(f"Removed element using pop(): {removed_element}, remaining set: {my_set}")

# Clearing all elements
my_set.clear()
print(f"After clearing the set: {my_set}")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (elements in either set)
union_set = set_a.union(set_b)
print(f"Union of A and B: {union_set}")
# Alternative using | operator
union_set_operator = set_a | set_b
print(f"Union using | operator: {union_set_operator}")

# Intersection (elements common to both sets)
intersection_set = set_a.intersection(set_b)
print(f"Intersection of A and B: {intersection_set}")

# Alternative using & operator
intersection_set_operator = set_a & set_b
print(f"Intersection using & operator: {intersection_set_operator}")

# Difference (elements in set_a but not in set_b)
difference_set = set_a.difference(set_b)
print(f"Diffrence (A - B): {difference_set}")
# Alternative_ using - operator
difference_set_operator = set_a - set_b
print(f"Difference using - operator: {difference_set_operator}")

# Symmetric Difference (elements in either set, but not in both)
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(f"Symmetric difference of A and B: {symmetric_difference_set}")
# Alternative using ^ operator
symmetric_difference_set_operator = set_a^set_b
print(f"Symmetric Difference of A and B using ^ operator:{symmetric_difference_set_operator}")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {6, 7}

#issubset()
print(f"Is set_x a subset of set_y?: {set_x.issubset(set_y)}")

# issuperset()
print(f"Is set_y a superset of set_x?: {set_y.issuperset(set_x)}")

# isdisjoint()
print(f"Are set_x and set_z disjoint?: {set_x.isdisjoint(set_z)}")



matrix = [[1,2,4], [3,5,6], [7,8,9]]
print(matrix[2][1])

data = ["Name", ["John Doe", 22], "City", "New York"]
print(data[1][0])


matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix[0][0] = 10
print(matrix)


main_list = []
sublist1 = [10,20]
sublist2 = ["a", "b", "c"]

main_list.append(sublist1)
main_list.append(sublist2)

main_list.insert(0, ["x", "y"])

matrix = [[j for i in range(3)] for j in range(3)]

numbers = [1,3,6]
nested_squares = [[x**2 for x in numbers], [y*2 for y in numbers]]

employees = {
    "emp001": {
        "name": "Manoj",
        "position": "Architect",
        "contact": {
    	    "email": "bob@gmail.xm",
	    "phone": "3785927493"
        }
    },
    "emp002": {
	"name": "Suraj",
	"position": "Sr. Manager",
	"contact": {
	    "email": "hod@somtng.com",
	    "phone": "27032750473"
        }
    }
}

print(employees["emp001"]["name"])
print(employees["emp002"]["contact"]["email"])

employees["emp001"]["position"] = "Senior Software Engineer"
employees["emp001"]["contact"]["phone"] = "7502750237"
print(employees["emp001"]["position"])
print(employees["emp001"]["contact"]["phone"])

del employees["emp002"]["contact"]
print(employees["emp002"])

students = {}
students["student1"] = {"name": "Charlie", "age": 29, "grade": "A+"}
students["student2"] = {"name": "Diana", "age": 33, "grade": "B-"}
print(students)

data = [
    ("item_A", "color", "red"),
    ("item_B", "color", "blue"),
    ("item_A", "size", "small")
]

inventory = {}
for item, attribute, value in data:
    if item not in inventory:
        inventory[item] = {}
    inventory[item][attribute] = value
print(inventory)

nested_dict_constructor = dict (
    outer_key1=dict(inner_key1="value1"),
    outer_key2=dict(inner_key2="value2"),
    outer_key3=dict(inner_key3="value3"),
)
print(nested_dict_constructor)


nested_tuple = (1,2,("a","b"),5)
print("nested_tuple")

matrix = ((1,2,3), (4,5,6), (7,8,9))
print(matrix)

print(nested_tuple[0])
print(nested_tuple[2][0])

print(matrix[1][2])

tuple_a = (1,5)
tuple_b = ("f", "h")

nested_tuple_4 = (tuple_a, tuple_b)

frozenset_a = frozenset({40,50})
frozenset_b = frozenset({"d","s","a"})
frozenset_c = frozenset({True, False})

set_of_frozensets = {frozenset_a, frozenset_b, frozenset_c}
print(set_of_frozensets)

nested_set_comprehension = {frozenset(range(i, i+3)) for i in range(1, 10, 4)}
print(nested_set_comprehension)


text = "   Hello,  World  "
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())
print(text.find("or"))
print(text.count("l"))
print(text.startswith("Hell"))
print(text.endswith("rld"))
print(text.strip())
print(text.replace("world", "duniya"))
print(text.split(","))


words = ["Hello", "World"]
print(" ".join(words))

print("Python43".isalnum())
print("Hiii".isalpha())
print("53243".isdigit())
print("hello".islower())
print("HELLO".isupper())
'''

#UNIT 3 & 4
'''
def double(x):
    print(2*x)
double(12)

#Generator Function
#Higher Order Functions (a function calling another function as a parameter or something)
#Lambda Functions
#Built-in Functions
#Recursive Functions
#User-defined Functions

double = lambda x: x*2
print(double(12))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

def count_up_to(limit):
    n=0
    while n <= limit:
        yield n
        n += 1
counter = count_up_to(4)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

def square(n):
    return n*n
numbers = [3,6,8]
squared_numbers = list(map(square, numbers))
print(squared_numbers)


#Positional Arguments
#Keyword Arguments
#Default Arguments
#Arbitrary Positional Arguments(*args)
#Arbitrary Keyword Arguments(`:kwargs`)

def greet(name, msg):
    print(f"Hello, {name}! {msg}")
greet("Bob", "Are you okay?")

def intro(name, age):
    print(f"Name: {name} and Age: {age}")
intro(age=23, name="Bob")

def say_hello(name="Siya"):
    print(f"Hey {name}")
say_hello()
say_hello("Doggo")

def sum(*numbers):
    total = 0;
    for num in numbers:
        total += num
    print(f"Sum: {total}")
sum(2,4,6,7,8)
sum(34,5,3)
sum()

def disp_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
disp_info(name="Dev", occupation="Developer", city="California")
disp_info(name="Pope Francis", state="Florida")
'''

#datetime Module
'''
import datetime
my_date = datetime.date(2025, 9, 30)
print(my_date)

my_time = datetime.time(15, 9, 30)
print(my_time)

current_datetime = datetime.datetime.now()
print(current_datetime)

date1 = datetime.date(2025, 9, 30)
date2 = datetime.date(2025, 10, 1)
difference = date2 - date1
print(difference)
'''

#Binary Data type
'''
byte_data = b"Hello"
print(byte_data)
print(type(byte_data))
print(byte_data[0])
try:
    byte_data[0] = 28
except TypeError as e:
    print(f"Error: {e}")

mutable_byte_data = bytearray(b"Hello")
print(mutable_byte_data)
print(type(mutable_byte_data))
mutable_byte_data[0] = 22
print(mutable_byte_data[0])
mutable_byte_data.append(ord('!'))
print(mutable_byte_data)

data = b"kamikaze"
mv = memoryview(data)
print(mv)
print(type(mv))
print(mv[1:4])

mutable_data = bytearray(b"kamikaze")
mutable_mv = memoryview(mutable_data)
mutable_mv[0] = ord('F')
print(mutable_data)
'''

'''
import struct

format_string = "<if10s"
integer_value = 124
float_value = 3.14
string_value = b"HelloWorld"

packed_data = struct.pack(format_string, integer_value, float_value, string_value)
print(f"Packed data: {packed_data}")

unpacked_data = struct.unpack(format_string, packed_data)
print(f"Unpacked data: {unpacked_data}")

size = struct.calcsize(format_string)
print(f"Size of packed data: {size} bytes")
'''



# Tkinter: It is a std library for creating gui, it contains set of tools and widgets to develop rich windows based desktop application
# Features of Tkinter: 
# it contatins all the necessary modules for developting GUI
# this is included with the std python installation
# cross platform compatibility
# Tcl/Tk interface: it is a lightweight wrapper around the Tcl/Tk toolkit for python to interact with the Tk functionalities
# it offers various prebuilt widgets such as buttons, labels, text areas, entry fields, frames, etc. which are building blocks for GUI
# layout management: it provides geometry managers to control, positioning and arrangment of the widgets withing a window or the frame
# Event handling: () Tkinter supports event handling which allows binding of interactions like clicks of a button or key press to a specific python function to make the application interactive 

'''
import tkinter as tk
root = tk.Tk()
root.title("My first tkinter app")
root.geometry("300x200")
label = tk.Label(root, text="hello")
label.pack(pady=20)

def on_button_click():
    label.config(text="clicked")
button = tk.Button(root, text="click here", command=on_button_click)
button.pack()
root.mainloop()
'''

'''
import tkinter as tk
def show_input(): 
    entered_text = entry.get()
    display_label.config(text=f"You entered: {entered_text}")
window = tk.Tk()
window.title("Entry field example")
window.geometry("300x200")
entry = tk.Entry(window, width=30)
entry.pack(pady=10)
button = tk.Button(window, text="Show input", command=show_input)
button.pack(pady=5)
display_label = tk.Label(window, text="")
display_label.pack(pady=10)
window.mainloop()
'''

'''
import tkinter as tk
from tkinter import messagebox
def on_button_click():
    messagebox.showinfo("clicked button")
window=tk.Tk()
window.title("Button Example")
window.geometry("300x200")
button = tk.Button(window, text="Click here", command=on_button_click)
button.pack(pady=30)
window.mainloop()
'''
# IOT is a network of connected physical objects embedded with censors, software and other data transmission technologies and these objects collect and exchange data with the internet integrating the physical system and the digital system. This enhances automation, efficiency and decision making.
# IOT libraries in python: The advantage of python being a cross platform language that can run on various operating systems as well as small devices like raspberry pi makes it capable of integration with the IOT landscape.
# Basic python libraries for IOT: MQTT(Message Queuing Telemetry Transport), Paho, Requests
# MQTT is a light weight messaging protocol designed for low bandwidth, high latency IOT devices. This library supports reliable message delivery. Use case: Smart home automation, vehicle to cloud communication, industrial IOT for real time monitoring 
# Paho is an official client library of MQTT which supports multiple protocols including MQTT-SN(Sensor Networks) and web sockets, it supports cross platform integration with various operating system, it has asynchronous and blocking modes giving flixibility to MQTT messaging 
# Requests is a simple python library for sending HTTP and HTTPS requests, it is used for connecting IOT devices to cloud servers. Fetching and sending data via REST api. Interaction with authentication protected IOT platform.
# Use of Requests in IOT: IOT dashborads displaying senor data, real time data collection for weather monitoring, remote device management using cloud services 
# Python's MQTT Paho and Requests provide realtime, scalable and secure communication between devices, servers and cloud platforms making it the backbone of IOT applications.

# Libraries in Python for CYBERSECURITY: CYBERSECURITY refers to all the aspects of protecting an organisation, its employees and assets against any cyber threat. Due to the increased number of corporate networks cyber attacks are more common and sophisticated. Python provides variety of libraries that can be utilised to mitigate these cyber risks, it provides standard libraries for various internet protocols including HTTP, SMTP, FTP, TELNET, etc. along with various 3rd party libraries used in cybersecurity
# Uses of Python in Cybersecurity: Penetration testing, malware analysis, network traffic analysis, security automation, forensic analysis, threat intelligence, password cracking

# Penetration testing: Python enables cybersecurity analysts to create scrips and tools for identifying, examining and exploiting vulnerablities of the system and network

# Malware analysis: the analyst can create scripts to detect and isolate suscpicious code which is known as malware

# Network traffic analysis: the analyst can create scripts to collect and analyse data package to .... in order to identify unususal behaviour

# Security automation: it is used to automate common security activities like log analysis, vulnerability detection and patch administration, the scripts run automatically and sends warning when a security incident occurs

# Forensic analysis(autopsy): it is used by analysts to write scripts , evaluate logs and system files for determining the cause of a security breach in the system.

# Threat intelligence: the analyst can write scripts delivering realtime alerts for potential hazards

# Password cracking: it is used to create scripts that can use bruteforce or other such techniques that is used for cracking passwords... analyst creates scripts to break the passwords using bruteforce techniques

'''
from Crypto.Cipher import AES
key = b'SuperSecurityKey1234567890'
cipher = AES.new(key, AES.MODE_EAX)
data = b'This is some sensitive data'
ciphertext, tag = cipher.encrypt_and_digest(data)
cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)
print(plaintext.decode('utf-8'))
'''

'''
import requests
response = requests.get('https://www.github.com/')
if response.status_code == 200:
    print("Request Successful")
else:
    print("Request Failed")
print("Headers:", response.headers)
print("Content:", response.text)
'''

'''
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
with open("output.txt", "r") as file:
    lines = file.readlines()
    print(lines)
with open("output.txt", "w") as file:
    file.write("This is the first line.")
    file.write("This is the second line.")
with open("output.txt", "a") as file:
    file.write("\nThis line is appended.")
lines_to_write = ["Line A/n", "Line B/n", "Line C/n"]
with open("new_file.txt", "w") as file:
    file.writelines(lines_to_write)
file = open("output.txt", "r")
content = file.read()
file.close()

with open("Python-Logo.png", "rb") as source_file:
    data = source_file.read()
with open("copy_image.png", "wb") as dest_file:
    dest_file.write(data)
try:
    with open("new_exclusive_file.txt", "x") as file:
        file.write("This file was exclusively created.")
except FileExistsError:
    print("File already exists")
with open("new_exclusive_file.txt", "r+") as file:
    content = file.read()
    file.seek(0) 
    file.write("NEW " + content)
'''

# import array as arr
# my_array = arr.array('i', [2,4,5,6])
# print(my_array)

# my_list = [x**2 for x in range(5)]
# print(my_list)

'''
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

data={'Name':['Alice','Bob','Charlie'],'Age':[25,30,35],'City':['New York','London','Paris']}
df=pd.DataFrame(data)
print("DataFrame from Dictionary")
print(df)

data=[['Alice',25,'New York'],['Bob',30,'London'],['Charlie',35,'Paris']]
df=pd.DataFrame(data,columns=['Name','Age','City'])
print('\nDataFrame form Lists to Lists:')
print(df)
'''



'''
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 37, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Select a single column
print("\nSelected 'Name' column:")
print(df['Name'])

# Select multiple columns
print("\nSelected 'Name' and 'City' columns:")
print(df[['Name', 'City']])

# Filter rows based on condition
print("\nRows where Age > 30:")
print(df[df['Age'] > 30])

# Add a new column
df['Occupation'] = ['Engineer', 'Designer', 'Doctor', 'Analyst']
print("\nDataFrame with new 'Occupation' column:")
print(df)
'''



'''
import pandas as pd
import numpy as np

#From a python list
arr1=np.array([1,2,3,4,5])
print("1D Array:",arr1)
print()

#2D Array(matrix) from a list of lists
arr2=np.array([[1,2,3],[4,5,6]])
print("2D Array:\n",arr2)
print()

#Array of zeroes
zeros_arr=np.zeros((2,3))
print("Zeros Array:\n",zeros_arr)
print()

#Array of ones
ones_arr=np.ones((3,2))

#Array with a range of values
range_arr = np.arange(10)  #0 to 9
print("Range Array: ", range_arr)

#Array with a specified data type
float_arr = np.array([1,2,3], dtype=float)
print("Float Array: ", float_arr)

arr = np.array([[1,2,3], [4,5,6]])
print("Shape:", arr.shape) #dimensions of the array (rows, columns)
print("Number of dimensions:", arr.ndim) #number of array dimensions
print("Data type:", arr.dtype) #datatype of the elements
print("Size (total elements):", arr.size) #total number of elements

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Element at (0,1):", arr[0,1])  #accessing an element
print("First row:", arr[0,:]) #slicing the first row
print("Second coloumn:" , arr[:,1]) #slicing the second coloumn
print("Sub-array (rows 0-1, cols 1-2):\n", arr[0:2, 1:3])

a = np.array([1,2,3])
b = np.array([4,5,6])
#element-wise addition
print("Addition:", a+b)
#element-wise multiplication
print("Multiplication:", a*b)
#scalar multiplication
print("Scalar multiplication:", a*2)
#dot product
dot_product = np.dot(a, b)
print("Dot product:", dot_product)
#sum of all elements
print("Sum of elements in 'a':", a.sum())
#mean of all elements
print("Mean of all elements in 'b':", b.mean())

arr = np.arange(12) # 0 to 11
print("Original Array:", arr)
reshaped_arr = arr.reshape(3,4) #reshape to 3 rows, 4 coloumns
print("Reshaped Array:\n", reshaped_arr)
'''





'''
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

#prepare some data
x= np.linspace(0,50,200) # 100 points between 0 to 10
y= np.sin(x) #sine wave of x

#create a figure and an axes object
fig, ax= plt.subplots()

#plot the data on the axes
ax.plot(x,y, label='sin(X)', color='blue', linestyle='-')

#addlables, title, and legend
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Sine Wave Plot')
ax.legend()

#add s grid for better readability
ax.grid(True)

#display the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt
xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.array([0,1,2,3,4,5])
y = np.array([0,2,4,6,8,10])

#Create the plot 
plt.plot(x,y)

#Add albels and titles
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.title("Simple Line Plot")

#Display the Plot
plt.show()
'''




'''
#First function definition
def double(x):
    """Double x"""
    return 2*x
x=double(2.5)
print(x)
x=double("a")
print(x)
x=double("riya ")
print(x)
x=double(4)
print(x)

"""Built-in functions, User-defined functions, Lambda(Anonymous) functions, Recursive functions, Generator functions, Higher-order functions"""

#Example of lambda fucntion
double = lambda x: x*2
print(double(5))

#Example of a recursive function (factorial calculation)
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

#Example of a generator function
def count_up_to(limit):
    n=0
    while n<=limit:
        yield n
        n += 1
counter=count_up_to(3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#Example of a higher-order function(using maps)
def square(x):
    return x*x
numbers=[1,2,3,4]
squared_numbers=list(map(square, numbers))
print(squared_numbers)

"""function arguments:  Positional(Required) Arguments, Keyword args., Default args., Arbitrary Positional args. (*args), Arbitrary Keyword args. (':kwargs')"""

#Positional args
def greet(name, message):
    print(f"Hello, {name}! {message}")
greet("Alice", "How are you?")

#Keyword args
def introduce(age, name):
    print(f"My name is {name} and I am {age} years old.")
introduce(age=30, name="Bob")

#Default args
def say_hello(name="Guest"):
    print(f"Hello, {name}!")
say_hello()
say_hello("Charlie")

#Arbitrary Positional args. (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"The sum is:{total}")
sum_all(1,2,3)
sum_all(10,20,30,40)
sum_all(1000,20000,20000,30002,6278,2762)
sum_all()
sum_all(10)

#Arbitrary Keyword args. (':kwargs')
def display_info(**details):
    for key,value in details.items():
        print(f"{key}: {value}")
display_info(name="David", occupation="Engineer", city="New York")
display_info(name="John", city="Yorkshire")
'''




'''
import datetime
my_date = datetime.date(2025, 9, 29)
print(my_date)  #o/p: 2025-09-29


#import datetime
my_time = datetime.time(10, 4, 30)
print(my_time)   #o/p: 10:04:30


#import datetime
current_datetime = datetime.datetime.now()
print(current_datetime)  #o/p: 2025-09-29 10:04:30.123456 (Example)


#import datetime
date1 = datetime.date(2025, 9, 29)
date2 = datetime.date(2025, 10, 5)
difference = date2 - date1
print(difference)    #o/p: 6 days, 0:00:00

"""Struct module: struct.pack(format, v1, v2 ....), struct.unpack(format,buffer), struct.calcsize(format), Format Strings, Bytes Objects, Tuples for Unpacking"""


#Creating a bytes object
byte_data = b"hello"
print(byte_data)
print(type(byte_data))

#Accessing individual bytes (returns an integer)
print(byte_data[0])

#Attempting to modify a bytes object will raise an error
try:
    byte_data[0] = 72
except TypeError as e:
    print(f"Error: {e}")

#Creating a bytearray
mutable_byte_data = bytearray(b"hello")
print(mutable_byte_data)
print(type(mutable_byte_data))

#Modifying the bytearray (ASCII value for 'H' is 72)
mutable_byte_data[0] = 72
print(mutable_byte_data)

#Appending to a bytearray
mutable_byte_data.append(ord('!'))
print(mutable_byte_data)

#Creating a memoryview from a bytes object
data = b"abcdefg"
mv = memoryview(data)
print(mv)
print(type(mv))

#Accessing a slice of the memoryview
print(mv[1:4])

#Modifying through a memoryview (if the underlying object is mutable)
mutable_data = bytearray(b"abcdefg")
mutable_mv = memoryview(mutable_data)
mutable_mv[0] = ord('A')
mutable_mv[5] = ord('B')
mutable_mv[3] = ord('R')
print(mutable_data)

import struct
#Define a format string:
#'<' indicates little-endiann byte order
#'i' for a signed integer (4bytes)
#'f' for a float (4bytes)
#'10s' for a string of 10 characters (10bytes)

format_string = '<if10s'
#1. Packing data into binary
#Values to pack: an integer, a float, and a bytes object (representing the string
integer_value = 123 
float_value = 3.14
string_value = b"HelloWorld" # Must be bytes for 's' format

packed_data = struct.pack(format_string, integer_value, float_value, string_value)
print (f"Packed data: {packed_data}")

#2. Unpacking binary data back into Python values
unpacked_data = struct.unpack (format_string, packed_data)
print (f"Unpacked data: {unpacked_data}")

#3. Calculating the size of the packed data
size = struct.calcsize(format_string)
print(f"Size of packed data: {size} bytes")
'''

