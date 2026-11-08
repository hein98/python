def square(num):
    return num * num


def cube(num):
    return num * num * num


def operate(nums, operation):
    for i in nums:
        result = operation(i)
        print(result)


nums = [5, 6, 7]
operate(nums, cube)

# 125
# 216
# 343
