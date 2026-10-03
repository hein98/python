a = 5
print(a)
print(id(a))
# 140718307517480

b = 5
print(id(b))  # refering the same box 5
# 140718307517480

b = 6
print(id(b))
# 140718307517512


c = 8 + 8j
print(type(c))

a = 2
b = 3
c = complex(a, b)
print(c)
# (2+3j)

######################

a = 7
b = 6

greater = b > a
print(greater)
# False

r = range(0, 10)
print(r)
print(type(r))
# <class 'range'>

print(set(r))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set(range(2, 12, 3)))
