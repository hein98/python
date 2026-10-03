nums = [4, 5, 6, 7, 8, 9, 10]

###FILTER
evens = list(filter(lambda i: i % 2 == 0, nums))
print(evens)
# [4, 6, 8, 10]

doubles = list(map(lambda n: n * 2, evens))
print(doubles)
# [8, 12, 16, 20]

 