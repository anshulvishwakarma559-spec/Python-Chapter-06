#Write a program that print all numbers from 100 to 1 using for and range().
a = 100 
for item in range(1,101):
    if (a>=1):
        print(a)
    a-=1


#other method 
for item in range(100,0,-1):
    print(item)