list = []
while True:
    print("1. Insert an element")
    print("2. Delete an element")
    print("3. Reverse the list")
    print("4. Pop an element")
    print("5. Sort the list")
    print("6. Count the distinct elements")
    print("7. Clear the list")
    print("8. Display the list")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = input("Enter the element to insert: ")
        list.append(element)
    elif choice == 2:
        element = input("Enter the element to delete: ")
        if element in list:
            list.remove(element)
        else:
            print("Element not found in the list.")
    elif choice == 3:
        list.reverse()
    elif choice == 4:
        index = int(input("Enter the index of the element to pop: "))
        if 0 <= index < len(list):
            list.pop(index)
        else:
            print("Index out of range.")
    elif choice == 5:
        list.sort()
    elif choice == 6:
        key = input("Enter the element to count: ")
        count = list.count(key)
        print("The element", key, "appears", count, "times in the list.")
    elif choice == 7:
        list.clear()
    elif choice == 8:
        print("The list is:", list)
    else:
        print("Exiting the program.")
        break
    