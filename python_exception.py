def divide():
    try:
        a = int(input("Ënter Any number"))
        b = int(input("Enter Any number"))
        print(a / b)

    except ZeroDivisionError:
        print("Give the value except zero")
        b = int(input("Enter Any number"))
        print(round(a / b), 2)

    except Exception as e:
        print(e)
    finally:
        print("Program Ended")


divide()
