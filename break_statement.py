#Break: the break statemnet stops the loop immediately when it is encountered.
#Example: 
for num in range(1,10):
    if num == 5: 
        break
    print(num)

#The break statement enables a  program to skip over a part of a code.
#A break statement terminates the very loop it lies within.

print("="*40)

#with examplee of multiplication table.

for i in range(1,10):
    if (i == 9):
        break
    print("5 X",i ,"=",5 * i)
    
print("="*40)

#practice 
j = 0
print("Practice")

while True:
    print(j)
    j += 1
    if j % 80 == 0:
        break 