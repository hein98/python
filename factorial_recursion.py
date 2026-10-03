def fact(num):

    if num == 1:
        return 1

    return num * fact(num - 1)  # recursion


result = fact(5)
print(result)
# 120
