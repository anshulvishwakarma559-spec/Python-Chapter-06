'''Write a program to print numbers from 1 to 50, but
 print"Anshul Vishwakarma!" instead of numbers that are multiples of 5.
 Example Output : 1 2 3 4 Anshul Vishwakarma 6 7 8 9 Anshul Vishwakarma....'''

for item in range(1, 51):
    if item % 5 == 0:
        print("Anshul Vishwakarma!", end=" ")
    else:
        print(item, end=" ")
print("Your practice 2 program has a successfully completed!\nThankyou!")


















for i in range(1,51):
    if i % 5 == 0:
        print("Anshul Vishwakarma",end =" ")
    else:
        print(i , end=" ")

