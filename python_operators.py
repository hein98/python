a = 3
b = 2

print(a + b)  # 5
print(a - b)  # 1

a = a + 2
print(a)
# 5

b += 6
print(b)
# 8
# '=' is assignment operator


a = 5
a = -a
print(a)
x, y = 4, 5
# -5
print(a < -a or x > y)
# -5 < -(-5)
# -5<5
# True

condition_1 = False
condition_2 = True
print(condition_1 and condition_2)
