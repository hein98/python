class A:

    def __init__(self):
        print("A Init Call")

    def function_1(self):
        print("F1 call")


class B(A):

    def __init__(self):
        super().__init__()
        print("B Init Call")

    def function_2(self):
        super().function_1()
        print("F2 call")


# obj1 = B()
# obj1.function_1()

# # A Init Call // also calls init from super class A
# B Init Call
# F1 call


ob2 = B()
ob2.function_2()
# A Init Call
# B Init Call
# F1 call
# F2 call
