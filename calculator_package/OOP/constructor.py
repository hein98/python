class Abc:

    def __new__(cls):
        print("Constructor Call")
        return super(Abc, cls).__new__(cls)

    def __init__(self):
        print("Init Called")

    def show(self):
        print("Show Function Call")


object_1 = Abc()
object_1.show()

object_2 = Abc.__new__(Abc)  # constructor
object_2.show()
# Show Function Call
