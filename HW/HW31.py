from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата {amount} сом через банковскую карту выполнена.")

    def refund(self, amount):
        print(f"Возврат {amount} сом на карту выполнен.")

class CryptoPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата {amount} сом через криптовалюту выполнена.")

    def refund(self, amount):
        print(f"Возврат {amount} сом через криптовалюту выполнен.")

card = CardPayment()
crypto = CryptoPayment()

card.pay(1000)
card.refund(500)

crypto.pay(2000)
crypto.refund(1000)
