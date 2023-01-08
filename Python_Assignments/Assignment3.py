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


########################## Task 6 ##########################
# Question 1
l = "abcdefgABCDEFGHIJKLMNOP"
new_str=''.join([c for c in l if c.isupper()])
print(new_str)

#2.
students = ["Smit","Jaya","Rayan"]
subjects = ["CSE","Networking","Operating System"]
print("The list of key is: " + str(students))
print("The list of value is: " + str(subjects))
output = dict(zip(students, subjects))
print("The new dictionary is: " + str(output))

# Question 3. Learn't about Yield,next and Generators.
#A generator is a function that returns a value through the keyword yield instead of return. To get the next value of a generator, we use the same function as for an iterator: next().
#Every time we call next() on a generator, the generator must transfer a value and the control through yield. 

# Question 4
def string_reverse(str):
    length = len(str)
    for x in range(length-1, -1, -1):
        yield str[x]
for ch in string_reverse("Consultadd Training"):
    print(ch,end='')

