# Ques1
length = float(input("Enter the length of the rectangle:"))
breadth = float(input("Enter the breadth of the rectangle:"))
area = length * breadth
print("The area of the rectangle is:", area)

# Ques2
principal = float(input("Enter the principal amount:"))
rate = float(input("Enter the rate of interest:"))
time = float(input("Enter the time in years:"))
simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)

# Ques3
celsius = float(input("Enter the temperature in Celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is:", fahrenheit)

# Ques4
num1 = 34
num2= 45
num3 = 12
average = (num1+num2+num3)/3
print("The average of the three numbers is:", average)

# Ques5
number = int(input("Enter a number:"))
square = number^2
cube = number^3
print("The square of the number is:", square)
print("The cube of the number is:", cube)

#Ques6
x = 10
y = 20
x,y = y,x
print("The value of x after swapping is:", x)
print("The value of y after swapping is:", y)

#Ques7
student_name= input("Enter the student name :")
student_id = input("Enter the student id :")
# initialize total marks and percentage
for i in range(5):
    marks = float(input("Enter the marks for subject {}:".format(i+1)))
    total_marks += marks
    percentage = (total_marks/500)*100

# print the student details and results
print("Student Name:", student_name)
print("Student ID:", student_id)
print("Total Marks:", total_marks)
print("Percentage:", percentage)