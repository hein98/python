a = 5
print(a.__str__())
# b = 6
# # c = a + b

# # c = int.__add__(a, b)
# c = a.__add__(b)

# print(c)


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}:{self.balance}"

    def __add__(self, other):
        return Account("combined", self.balance + other.balance)


user1 = Account("Hein", 100)
user2 = Account("Fern", 50)

combined = user1 + user2

print(user1)
print(user2)
print(combined)

# 5
# Hein:100
# Fern:50
