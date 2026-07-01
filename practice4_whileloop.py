#Practice Question 04: Write a python program that print the sum of first n natural numbers.

n = int(input("Enter the value of n:"))
sum = 0
while n>=1:
    sum = sum+n
    n-=1
    print("sum: ",sum)
    print("n:",n)
print("Your 4th program has a completed!\nThankyou!")