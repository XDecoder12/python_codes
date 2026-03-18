#Find the factors of a number
number = int(input("Enter the number: "))
for i in range(1,(number+1)):
    if((number%i) == 0):
        print(i)


#Generate Pascal Triangle
rows = int(input("Enter the number of rows: "))
pattern = []
for i in range(rows):
    row = [1]
    if i > 0:
        for j in range(1, i):
            row.append(pattern[i-1][j-1] + pattern[i-1][j])
        row.append(1)
    pattern.append(row)
for row in pattern:
    print(row)


#Find HCF and LCM of 2 numbers
def hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    HCF = hcf(a, b)
    return (a * b) // HCF

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("HCF =", hcf(num1, num2))
print("LCM =", lcm(num1, num2))


#Fibonacci series using function
def fibon(t):
    if t<=1 :
        return t
    else: 
        return fibon(t-1) + fibon(t-2)
n = int(input("Enter no. of terms: "))
for i in range(n):
    print(fibon(i))


#User-defined function Calculator
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

def mean(numbers):
    return sum(numbers) / len(numbers)

def is_leap_year(year):
    if (year % 4 == 0):
        return True
    else:
        return False

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def profit_or_loss(cost_price, selling_price):
    if selling_price > cost_price:
        return f"Profit = {selling_price - cost_price}"
    elif cost_price > selling_price:
        return f"Loss = {cost_price - selling_price}"
    else:
        return "No Profit No Loss"

def area_square(side):
    return side * side

def area_rectangle(length, breadth):
    return length * breadth

def area_triangle(base, height):
    return 0.5 * base * height

def calculator():
    print("CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Palindrome Check")
    print("6. Mean of Numbers")
    print("7. Leap Year Check")
    print("8. Simple Interest")
    print("9. Profit or Loss")
    print("10. Area Calculations")

    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", addition(a, b))

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", subtraction(a, b))

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", multiplication(a, b))

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", division(a, b))

    elif choice == 5:
        s = input("Enter a string or number: ")
        if is_palindrome(s):
            print(f"{s} is a Palindrome.")
        else:
            print(f"{s} is not a Palindrome.")

    elif choice == 6:
        nums = list(map(float, input("Enter numbers separated by space: ").split()))
        print("Mean =", mean(nums))

    elif choice == 7:
        year = int(input("Enter year: "))
        if is_leap_year(year):
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is not a Leap Year.")

    elif choice == 8:
        p = float(input("Enter Principal: "))
        r = float(input("Enter Rate of Interest: "))
        t = float(input("Enter Time (in years): "))
        print("Simple Interest =", simple_interest(p, r, t))

    elif choice == 9:
        cp = float(input("Enter Cost Price: "))
        sp = float(input("Enter Selling Price: "))
        print(profit_or_loss(cp, sp))

    elif choice == 10:
        print("a. Area of Square")
        print("b. Area of Rectangle")
        print("c. Area of Triangle")
        sub_choice = input("Enter your choice (a/b/c): ").lower()

        if sub_choice == 'a':
            side = float(input("Enter side: "))
            print("Area of Square =", area_square(side))
        elif sub_choice == 'b':
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            print("Area of Rectangle =", area_rectangle(l, b))
        elif sub_choice == 'c':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Area of Triangle =", area_triangle(base, height))
        else:
            print("Invalid Choice!")
    else:
        print("Invalid Option! Please try again.")

calculator()