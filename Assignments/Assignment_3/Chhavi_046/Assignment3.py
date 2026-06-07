
from email.mime import text

#ques1
def natural_numbers(n):
    for i in range(1, n+1):
        print(i)

natural_numbers(10)        

#ques2
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i
    return sum

print(f"The sum of first 10 natural numbers is: {sum_of_natural_numbers(10)}")
    
#ques3
def reverse(n):
    res = 0
    while n>0:
        digit = n%10
        res = res*10 + digit
        n = n//10
    return res

print(f"The reverse of 1234 is: {reverse(1234)}")

#ques4
def count_digits(n):
    count = 0
    while n>0:
        n = n//10
        count +=1
    return count

print(f"The number of digits in 1234 is: {count_digits(1234)}")

#ques5
def palindrome(n):
    num = n
    res = 0
    while(n>0):
        digit = n%10
        res = res*10 + digit
        n=n //10

    if num == res:
        return True    
    else:
        return False
    
print(f"Is 12321 a palindrome? {palindrome(12321)}")

#ques6
def fibonnaci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a+b

print(f"The first 10 numbers in the Fibonacci sequence are: ", end='')
fibonnaci(10)
print()  # Print a newline

#ques7
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
    

result = calculator()
print(f"The result is: {result}")

#ques8
with open("student.txt", "w") as f:
    f.write("Chhavi, 85")

#ques9
with open("student.txt", "r") as f:
    content = f.read()
    print(content)

#ques10
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#ques11
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student1 = Student("Chhavi", 85)
student1.display_info()
