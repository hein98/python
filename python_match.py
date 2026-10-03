age = int(input("Enter Any number: "))

match age:
    case age if 0 < age < 10:
        print("Child")

    case age if 10 < age < 20:
        print("Teenager")

    case age if 20 < age < 30:
        print("Adult")

    case _:
        print("Invalid")
