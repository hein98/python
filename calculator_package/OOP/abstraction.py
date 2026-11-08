from abc import ABC, abstractmethod


class TeluskoPay:
    def pay(self):
        print("Telusko Pay")


class RazorPay:
    def pay(self):
        print("Pay function call")


class Purchase:

    def __init__(self, gateway):
        self.gateway = gateway

    def checkout(self):
        print("Checking out...")

        self.gateway.pay()


gateway_1 = RazorPay()
gateway_2 = TeluskoPay()
purchase = Purchase(gateway_1)
purchase.checkout()
