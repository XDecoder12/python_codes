num = int(input("Enter a number: "))
if (num%2 == 0):
    print("The number is even.")
else :
    print("The number is odd.")


inp = input("Enter the number or string: ")
if (inp == inp[::-1]):
    print("It is a palindrome.")
else:
    print("It isn't a palindrome.")


text = input("Enter the string: ")
vowels = "aAeEiIoOuU"
print("Vowels in string: ")
for char in text:
    if char in vowels:
        print(char)


num = int(input("Enter the no. of terms: "))
a,b = 0,1
print("Fibonacci Series: ")
for i in range(num):
    print(a)
    a,b = b, a+b