class A:
    def function_1(self):
        print("F1 call")

    def function_2(self):
        print("F2 call")


class B:
    def function_3(self):
        print("F3 call")

    def function_4(self):
        print("F4 call")


class C(A, B):
    def function_5(self):
        print("F5 call")


ob1 = C()
ob1.function_1()
# F1 call

ob2 = C()
ob2.function_4()
# F4 call
