num1 = 44 #this is a int
text = 'This is a string' #this is a string
num2 = 10.5 #this is a float
num3 = True #this is bool data type
print(num1, type(num1))
print(text)
print(num2, type(num2))
print(num3, type(num3))


print("Addition",1+3) #this is addition
print("Substraction",50-5) #this is substraction
print("Modulus",7%3) #this is modulo operator
print("Floor Division",19//3) #this is lif
print("Exponent",4**9) #this is power operator


no1=int(input("Enter the first number: "))
no2=int(input("Enter the second number: "))
no3=int(input("Enter the third number: "))
if no1>=no2 & no1>=no3:
    print("The greatest number is: ",no1)
elif no2>=no1 & no2>=no3:
    print("The greatest number is: ",no2)
else:
    print("The greatest number is: ",no3)


string = str(input("Enter the string: "))
print(string.lower())
print(string.upper())
print(len(string))
print(string.strip())
print(f"Capitalize: '{string.capitalize()}'")
print(f"Strip Whitespace: '{string.strip()}'")
print(f"Replace 'me' with 'you': '{string.replace('me', 'you')}'")
print(f"Starts with 'Ho': '{string.startswith('Ho')}'")
print(f"Ends with 'ing': '{string.endswith('ing')}'")


string = str(input("Enter the string: "))
def count(s):
    return len(s.split())
print(count(string))
    

string = str(input("Enter the string: "))
print(string[1], string[2], string[5], string[11])
print(string[2:5])
print(string[::-1])
print(string[:100:2])