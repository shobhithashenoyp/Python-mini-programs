import sys
while True:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
        
    print("Select an operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor division")
    print("7. Exponentiation")
    print("Any other key to Exit")
    choice = input("Enter choice (1,2,3,4,5,6,7): ")
        
    if choice == "1":
        print(a+b)
    elif choice == "2":
        print(a-b)
    elif choice == "3":
        print(a*b)
    elif choice == "4":
        if b!=0:
            print(a/b)
        else:
            print("Error")
    elif choice == "5":
        if b!=0:
            print(a%b)
        else:
            print("Error")
    elif choice == "6":
        if b!=0:
            print(a//b)
        else:
            print("Error")
    elif choice == "7":
        print(a**b)
    else:
        sys.exit("Exiting the program.")
