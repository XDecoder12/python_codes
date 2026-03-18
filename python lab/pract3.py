#Write a program to create, append and remove lists in python and also to search the number of times a particular number occurs in a list

numbers = [1,2,4,3,4,5]
print("List: ", numbers)
numbers.append(6)
print("Appended List: ", numbers)
numbers.remove(2)
print("After removing List: ", numbers)
num_to_search = 4
count = numbers.count(num_to_search)
print(f"Required number occurs {count} times in the list")


#Demonstrate a python program that utilizes all the Dictionary Methods

employee = {"name": "Suraj Malhotra", "Salary": 35000, "Position": "Manager"}
print(employee)
copy_dict = employee.copy()
print("Copied Dictionary:", copy_dict)
print("Get age:", employee.get("age"))
print("Items:", employee.items())
print("Keys:", employee.keys())
print("Values:", employee.values())
employee.update({"Salary": 40000})
print("after_update:", employee)
employee.pop("Salary")
print("after_pop:", employee)
employee.popitem()
print("after_popitem:", employee)

keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 1)
print("Fromkeys_Dictionary:", new_dict)

copy_dict.clear()
print("after_clear:", copy_dict)


#Write a Python program to take marks of 5 subjects in a nested dictionary from the user and print obtained grades for 3 students input.

students = {}
for i in range(1, 4):
    print()
    name = input(f"Enter name of student {i}: ")
    subjects = {}
    for subject in ["Physics", "Chemistry", "Maths", "English", "Computer"]:
        marks = int(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks
    students[name] = subjects

print("\nStudent's Grades:")
for name, marks in students.items():
    total = sum(marks.values())
    percentage = total / 5
    if percentage >= 90:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "Fail"
    print(f"{name}: {grade} ({percentage:.2f}%)")


# Take two unique lists L1 and L2 Create L3 from L1 and L2 and combine L1 and L2 print only odd index number value. Create L4 from L1 & L2 by performing merge sort on them.

L1 = [10, 70, 50, 30]
L2 = [20, 40, 60, 80]
print("L1:", L1)
print("L2:", L2)

L3 = L1 + L2
print("Combined L3:", L3)

odd_index_values = [L3[i] for i in range(len(L3)) if i % 2 == 1]
print("Odd Index Values from L3:", odd_index_values)

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
L4 = L1 + L2
merge_sort(L4)
print("L4 after Merge Sort:", L4)


# Create 3D array and perform the following operations
# 1. Replace a single value
# 2. Extract 2x2 array and store it in another variable
# 3. Add two arrays
# 4. Take sum of all the elements of an array

import numpy as np
arr = np.array([[[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],
                
                [[10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]]])

print("3D Array:\n", arr)

arr[0, 1, 2] = 79
print("\nAfter Replacing arr[0,1,2] with 79:\n", arr)

sub_array = arr[0, 0:2, 0:2]
print("\nExtracted 2x2 Sub-array:\n", sub_array)

arr2 = np.ones((2, 3, 3), dtype=int) * 5
sum_array = arr + arr2
print("\nSum of both Arrays:\n", sum_array)

total_sum = arr.sum()
print("\nSum of all elements in arr:", total_sum)