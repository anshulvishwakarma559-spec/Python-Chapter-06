#You are given a list of Khushi Mehra favorite foods. write a program to print each food item using a for loop. 

foodList = ["kitkat","onion","chips"]
for item in foodList:
    print("Your favorite food is:",item)

#Advamced method: 
foodList = ["kitkat","onion","chips"]
for i, item in enumerate(foodList, start=1):
    print(f"Favorite food {i}: {item}")