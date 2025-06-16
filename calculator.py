print("Welcome to the calculator program")
m = input("Enter your first number:")
n = input("Enter your second number:")
print("1.Addition: ")
print("2.Subtraction: ")
print("3.Multiplication: ")
print("4.Division: ")
print("5.Floor division: " )

choice = input("Enter your choice:")

match choice:
    case "0":
        print("Invalid choice")
    case "1":
        print(int(m) + int(n))
    case "2":
        print(int(m) - int(n))
    case "3":
        print(int(m) * int(n))
    case "4":
        print(int(m) / int(n))
    case "5":
        print(int(m) // int(n))

print("Let us know what is your feedback regarding this program")  #This is a comment
