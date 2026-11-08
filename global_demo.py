a = 10


def something():
    globals()["a"] = 35
    a = 15
    print(f"inside {a}")


something()

print("outside: ", a)

# inside 15
# outside:  35
