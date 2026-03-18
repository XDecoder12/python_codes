#finding the greatest of 3 numbers

def greatest(x,y,z):
    if x>y and x>z:
        print(x," is the greatest number")
    elif y>x and y>z:
        print(y," is the greatest number")
    else:
        print(z," is the greatest number")

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
z=int(input("Enter the third number: "))
greatest(x,y,z)

#calculator

def calculator(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b != 0:
                return a/b
            else: 
                print("Division by zero error")

x=int(input("Enter a: "))
y=int(input("Enter b: "))

print("Addition:", calculator(x, y, "+"))
print("Subtraction:", calculator(x, y, "-"))
print("Multiplication:", calculator(x, y, "*"))
print("Division:", calculator(x, y, "/"))

#even or odd

def checker(num):
    if num % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"

print(checker(1))


