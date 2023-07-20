import calendar

while True:
    print()
    print("=== Welcome to python Calendar ===")
    yy = int(input("Enter year : "))
    mm = int(input("Enter month: "))
    print()
    print(calendar.month(yy, mm))

    next = input("Do you want to see more? (yes/no): ")
    if next == "no":
        print()
        print("Thanks for using calendar....")
        print()
        break
    else:
        pass