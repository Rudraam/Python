import time
import os
# lets make a small ice cream shop using python
print("==============================================================")
print("==============================================================")
a = "Welcome to Rudy's Ice Cream"
print(a.center)
print("==============================================================")
print("==============================================================")

c_name = input("Can I get the name for Order: ")
print("Hello " , c_name , "Welcome to Rudy's Ice Cream")
print("==============================================================")
print(c_name , "Here are the flavours, choose any one you want:")
print("1. Chocolate")
print("2. Vanilla")
print("3. Strawberry")
print("4. Belgium Chocolate Chip")
print("5. Mango")
choice = input("Choose Your Ice cream flavour: ")
print("==============================================================")

match choice:
    case "1":
        print("You have chosen Chocolate Ice Cream")
        print("Price: $2.99")
    case "2":
        print("You have chosen Vanilla Ice Cream")
        print("Price: $2.99")
    case "3":
        print("You have chosen Strawberry flavor")
        print("$2.99")
    case "4":
        print("You have chosen Belgium Chocolate Chip")
        print("Price: $3.99")
    case "5":
        print("You have chosen Mango flavor")
        print("Price: $2.99")
    case _:
        print("Invalid choice, please choose from the options above")
 
print("Anything else you would like to order?")
print("1. Yes")
print("2. No")
choice2 = input("Enter your choice(Y/N): ")
match choice2:
    case "Y":
        print("You have chosen to order more items")
        print("Here are some shakes if you prefer: ")
        print("1. Chocolate Shake")
        print("2.Pina Colada")
        print("3. Strawberry Shake")
        shake_c = input("Choose your shake: ")
        match shake_c:
            case "1":
                print("You have chosen Chocolate Shake")
                print("Price: $6.99")
            case "2":
                print("You have chosen Pina Colada")
                print("Price: $7.99")
            case "3":
                print("You have chosen Strawberry Shake")
                print("Price: $7.99")
            case "N":
                print("You have chosen not to order anything else")
            case _:
                print("Invalid choice. Please choose a valid option.")
           