list1 = [23, 'String', 2.4, 4 + 5j]
# print(type(list))


# Question 2
list2 = [46, 65, 37, 45, 50]
print(list2[:3])
print(list2[::3])
print(list2[3:])
print(list2[-1:])
print(list2[:-1])


# Question 3
list_sum = 0
list_prod = 1

for i in range(0, len(list2)):
    list_sum = list_sum + list2[i]
    list_prod = list_prod * list2[i]

print("Sum of list Items", list_sum)
print("Product of list items ", list_prod)


# Question 4
largest = max(list2)
smallest = min(list2)

print(largest)
print(smallest)


# Question 5
list3 = [27, 84, 23, 22, 45, 67, 88, 21, 20]

odd_list = list(filter(lambda x: (x % 2 != 0), list3))
print(odd_list)


# Question 6
list4 = list()

for i in range(1, 31):
    if (i <= 5 or i >= 25):
        list4.append(i ** 2)
    
print(list4)


# Question 7
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li2 = [21, 22, 23, 24, 25]

li[-1:] = li2

print(li)


# Question 8
a={1:10,2:20} 
b={3:30,4:40}
print(a)
print(b)
# c = a.update(b)
print("After updating a with b", a)


# Question 9
n = int(input("Enter dict size "))
dict1 = dict()
for i in range(1, n + 1):
    dict1[i] = i*i

print(dict1)


# Question 10
val = input("Enter values seprated by comas \n")

l = val.split(",")
tuple1 = tuple(l)

print(l)
print(tuple1)


############################# Task 4 #############################

# Question 1
s = input("Enter string \n")
print(s)

s2 = s[::-1]
print(s2)


# Question 2
s = input("Enter string \n")
uppercase = 0
lower = 0

for c in s:
    if (c >= 'a' and c <= 'z'):
        uppercase = uppercase + 1
    
    if (c >= 'A' and c <= 'Z'):
        lower = lower + 1
    
print("lowercase = ", lower)
print("uppercase = ", uppercase)


# Question 3
def unique(lists):
    l = []
    for a in lists:
        if a not in l:
            l.append(a)
    
    return l

lista = input("Enter string \n")
print(lista)

lista2 = unique(lista)
print(lista2)


# Question 4
items1 = [i for i in input().split('-')]

items1.sort()

print(items1)


# Question 5
lines = [i for i in input().split(' ')]
new_lines = []

for i in lines:
    new_lines.append(i.upper())

print(new_lines)


# Question 6
num_1 = input("Enter number ")
num_2 = input("Enter number ")

sum = int(num_1) + int(num_2)

print(sum)