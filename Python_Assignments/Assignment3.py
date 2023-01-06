################ Task 5 ###########################

# Question 1
a = 10
b = 20


# try:
#     if (a < b)
#         print('a is less than b')

#     c = 30
#     print(c)
# except SyntaxError:
#     print("Syntax error is handled")
    

# Question 2
import sys

try:
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("Incorrect name of the file please enter correct name")
    

# Question 3
try:
    num_1 = int(input("Enter number "))
    if (num_1 > 9999 or num_1 < 1000):
        raise ValueError
except ValueError:
    print("The length is too short/long !!! Please provide only four digits")
    
    
# Question 4
print('Enter correct username and password combo to continue')
count = 0

password = ""
username = ""

while password!='Harsh123' and username!='bank_admin' and count < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if password=='Hytu76E' and username=='bank_admin':
     print('Access granted')
     break

    else:
        print('Access denied. Try again.')
        count+=1 


# Question 6
with open('doc.txt') as f:
    lines = f.readlines()
    
print(lines)

line1 = ""

for line in lines:
    if( len(line) % 2 == 1):
        line1 = line

print(line1)


