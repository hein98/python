def outer():
    print("Outer func calling")

    def inner(x):
        print("Inner func calling", x)

    return inner


something = outer()
something(5)
