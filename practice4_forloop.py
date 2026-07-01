#Write a program that print the multiplication table of any number entered by user using a for loop.

a = int(input("Enter a number"))
b = 1
for item in range(1,11):
    if (b<=10):
        print(f"{a}x{b} = {a*b}")
    b+=1
print("Your program 4 has a successfully cmopleted!\nThankyou!")
