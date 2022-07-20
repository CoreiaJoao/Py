print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
total_price = 0
S = 15
M = 20
L = 25
cheese = 1
peperoni = 0

if size == "S":
    peperoni = 2
    if add_pepperoni == "Y" and extra_cheese=="Y":
        total_price=cheese+peperoni+S
        print(f"Your final bill is: ${total_price}.")
    if add_pepperoni == "Y"  :
        total_price+=peperoni
        if extra_cheese=="N" :
            total_price+=S
            print(f"Your final bill is: ${total_price}.")
    if add_pepperoni == "N"  :
        if extra_cheese=="Y" :
            total_price =cheese+S
            print(f"Your final bill is: ${total_price}.")
    if add_pepperoni=="N" :
        if extra_cheese=="N":
            total_price=S
            print(f"Your final bill is: ${total_price}.")

if size=="M" :
    peperoni=3
    if add_pepperoni == "Y" and extra_cheese=="Y":
        total_price=+peperoni+cheese+M
        print(f"Your final bill is: ${total_price}.")
    if add_pepperoni == "Y"  :
        total_price+=peperoni
        if extra_cheese=="N" :
            total_price+=M
            print(f"Your final bill is: ${total_price}.")
    if add_pepperoni == "N"  :
        if extra_cheese=="Y" :
            total_price =cheese+M
            print(f"Your final bill is: ${total_price}.")
    if add_pepperoni=="N" :
        if extra_cheese=="N":
            total_price=M
            print(f"Your final bill is: ${total_price}.")

 
if size=="L" :
    peperoni=3
    if add_pepperoni == "Y" and extra_cheese=="Y":
        total_price=+peperoni+cheese+L
        print(f"Your final bill is: ${total_price}.")
    if add_pepperoni == "Y"  :
        total_price+=peperoni
        if extra_cheese=="N" :
            total_price+=L
            print(f"Your final bill is: ${total_price}.")
    if add_pepperoni == "N"  :
        if extra_cheese=="Y" :
            total_price =cheese+L
            print(f"Your final bill is: ${total_price}.")
    if add_pepperoni=="N" :
        if extra_cheese=="N":
            total_price=L
            print(f"Your final bill is: ${total_price}.")
