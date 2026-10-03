class Computer:

    brand = "APPLE"

    def __init__(self, cpu, ssd, brand):
        self.cpu = cpu
        self.ssd = ssd
        self.brand = brand

    def config(self):
        return self.cpu, self.ssd, self.brand

    @classmethod
    def info(cls):
        return cls.brand

    @staticmethod
    def gb_to_bytes(gb):
        return gb * 1000


com1 = Computer("i5", "1TB", "MSI")
com2 = Computer("i7", "512GB", "Dell")
print(com1.config())
print(com2.config())


# ('i5', '1TB', 'MSI')
# ('i7', '512GB', 'Dell')
# In python __init__ is called by default whenever the obj is created.

print(Computer.info())
print(Computer.gb_to_bytes(16))
