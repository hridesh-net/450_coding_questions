############################ Task 1 #######################

# Question 1
a = 20
print(a, " ")
print(type(a))
print("\n")

b = 2.6
print(b)
print(type(b))
print("\n")

c = "string"
print(c)
print(type(c))
print("\n")


# # Question 2
complex = 4 + 5j
print(complex)
print(type(complex))
print("\n")

temp = complex
complex = a
a = temp
print("complex =", complex)
print(type(complex))
print("a =", a)
print(type(a))
print("\n\n")


# # Question 3
num1 = 46
num2 = 5
print("num1 =", num1)
print("num2 =", num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("num1 =", num1)
print("num2 =", num2)
print("\n\n")


# # Question 5
num_1 = int(input("Enter number 1 from 1_10 "))
num_2 = int(input("Enter number 2 from 1_10 "))

z = num_1 + num_2
result = 30 + z
print(result)
print("\n\n")


# Question6
temp = input("Enter value ")

print(type(temp))
print("\n\n")


########################## Task 2 #############################

# Question 1
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Consultadd - Python Training")
elif num % 3 == 0:
    print("Consultadd")
elif num % 5 == 0:
    print("Python Training")
else:
    print("Number is not divisible by 3 or 5")

# Question 2

operation = int(input(
    "Enter 1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication, 5 for Average: "))
if operation == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 + num2
    if result < 0:
        print("NEGATIVE")
    else:
        print(result)
elif operation == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 - num2
    if result < 0:
        print("NEGATIVE")
    else:
        print(result)
elif operation == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    if result < 0:
        print("NEGATIVE")
    else:
        print(result)
elif operation == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 * num2
    if result < 0:
        print("NEGATIVE")
    else:
        print(result)
elif operation == 5:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = (num1 + num2) / 2
    if result < 0:
        print("NEGATIVE")
    else:
        print(result)
else:
    print("Invalid")


# Question 4

while True:
    num = int(input("Enter a number: "))
    if num < 0:
        print("It's Over")
        break
    else:
        print("Good Going")
        continue
    

# Question 5

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=",")


# Question 7
for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    else:
        print(i, end=" ")


# Question 8

string = input("Enter a string: ")
letters = 0
digits = 0
for i in string:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
print("Letters", letters)
print("Digits", digits)


# Question 9
import random

lucky_number = 7
while True:
    number = int(input("Guess the lucky number: "))
    if number == lucky_number:
        print("Congrats! You guessed it right.")
        break
    else:
        answer = input("Do you want to guess again? (yes/no): ")
        if answer == "no":
            print("It's Over")
            break
        else:
            continue

number =int(input("Guess the lucky number: "))
lucky_number =random.randint(1, 10)
while True:
    if number == lucky_number:
        print("Good guess!")
        break
    else:
        print("Try again!")
        continue
        
        
# Question 10

answer =random.randint(1, 10)
print(answer)
number = int(input("Guess the lucky number: "))
while True:
    if number == answer:
        print("Good guess!")
        break
    else:
        print("Try again!")
    flag = str(input("Want to continue"))
    if flag == "no":
        print("Game over!")
        break
    else:
        continue

number = int(input("Guess the lucky number: "))
lucky_number = random.randint(1, 10)
counter=0
while counter<5:
    counter+=1
    if number == lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
        continue
print("Game over!")


# Question 11

number = int(input("Guess the lucky number: "))
lucky_number = random.randint(1, 10)
counter=0
while counter<5:
    counter+=1
    if number == lucky_number:
        print("Good guess!")
        break
    else:
        print("Try again!")
        continue
print("Sorry but that was not very successful")