#Introduction to loops 

'''
Loops in Python are used to execute a block of code repeatedly.
They help in reducing repetitive code and are useful for iteration.

In Python, loops are used to repeat a block of code multiple times.
They help perform tasks like printing a message several times, iterating over lists, or generating patterns.
'''

#Example: 
print("Hello Anshul!")
print("Hello Anshul!")
print("Hello Anshul!")
print("Hello Anshul!")
print("Hello Anshul!")

#Instead of writing this five time, we can use a loop.

#While Loop:  A while loop runs as long as a condition is True.
#Syntax: while condition:
#             block of code
 
#Example: 

i = 0
while i <= 10:
    print("Hello Anshul Vishwakarma!")
    i += 1
print (" You are out of the while loop range!")

print("="*40)

#Practice: 
print("Practice:")
j = int(input("Enter a number (<=50 to continue): "))
while j <= 50:
    print(j)
    j = int(input("Enter a number (<=50 to continue): "))
print("Done!")

print("="*40)

#Decrement loop Example: 
print("Decrement loop:")
k = 5
while k > 0:
    print(k)
    k -= 1

print("="*40)

#Using else condition with while loop:
print("else with while loop")
l = 5
while l > 0:   #jese hi while loop ki condition false hogi iske baad else ki condition execute hogi.
    print(l)
    l -= 1
else: 
    print("I am inside else")
    
print("="*40)