#Ques1
sum = 0
for i in range(1,11):
    sum +=i
print("The sum of first 10 natural numbers is:",sum)

#Ques2
fact = 1
num = 5
for i in range(1,num+1):
    fact*=i
print("The factorial of {} is: {}".format(num, fact))

#Ques3
fib1, fib2 = 0, 1
n = 10
print("The first {} numbers in the Fibonacci sequence are:".format(n))
for i in range(n):
    print(fib1, end=' ')
    fib1, fib2 = fib2, fib1 + fib2
print()

#Ques4
a =23
b=45
c =67
if a>b and a>c:
    print("{} is the largest number.".format(a))
elif b>a and b>c:
    print("{} is the largest number.".format(b))
else:
    print("{} is the largest number.".format(c))


#Ques5
student_name = input("Enter the student's name:")
total = 0
for i in range(5):
    score = float(input("Enter the score for subject {}:".format(i+1)))
    print("Score for subject {}: {}".format(i+1, score))
    total +=score
    percentage = (total/500)*100
print("Total score: {}".format(total))
print("Percentage: {}".format(percentage))

if(percentage >= 90):
    print("Grade: A")
elif(percentage >= 80):
    print("Grade: B")
elif(percentage >= 70):
    print("Grade: C")
else:
    print("Grade: E")