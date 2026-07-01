#for loop 

'''
A for loop is used to iterate(go through) sequences like lists, tuples, or strings.
Syntax: 
for element in sequence:
    code block
'''

#Example:
print("Example  food_list:") 
food_list = ["cake","mango","pizza"]
for item in food_list:
    print(item)

print("="*40) 

print("Example  like_tuple")
like_tuple = ("Bhopal","Indore","Salamatpur")
for each_item in like_tuple: 
    print("Cities visited by Anshul",each_item)

print("="*40)

#for loop using range() function : The range() function generates a sequence of numbers.
'''It is often used with loops.
Syntax : 
range(start, stop, step)
- start - beginning number(default = 0)
- stop  - end limit(excluded)
- step  - increment value(default = 1)
'''

#Example : 
print("for loop using range()")
for item in range(1,7):
    print(item)

for it in range(2,23,10):
    print(it)

print("="*40)

#Practice: 
print("Practice")
name = input("Enter your name: ")

for i in name:
    print(i)

print("="*40)

#Using if condition and input method: -string 
print("Using if condition and input method")

for j in name: 
    print(j)
    if j.lower() == "u":
        print("Found 'u'")
print("="*40)

#Practice-
print("Colors:")
colors = ["Red","Green","Yellow","Black"]
for color in colors:
    print("Color:", color)
    for char in color:
        print(" ", char)

print("="*40)

#Practice: 
print("range():")

for l in range(6):
    print(l+1)
   # print(l)

print("="*40)

for m in range(1,21):  #1 to 20 
    print(m)

print("="*40)

for n in range(1,201,20):  #1 to 200 with difference 20 
    print(n)

print("="*40)

