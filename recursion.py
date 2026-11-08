def greet():
    print("Hello")
    greet()


greet()
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
