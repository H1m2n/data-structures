from abc import abstractmethod

# abstract class
from design_patterns.bridge_design_pattern.payment_gateway import IPaymentGateway


class PaymentMethod:
    @abstractmethod
    def make_payment(self):
        pass


# refined abstract classes
# These classes should have the reference of implementer interface to connect with the implementation at run time
class CardPaymentMethod(PaymentMethod):
    def __init__(self, gateway: IPaymentGateway):
        self.gateway = gateway

    def make_payment(self):
        return self.gateway.process_payment('using card')


class NetBankingPaymentMethod(PaymentMethod):
    def __init__(self, gateway: IPaymentGateway):
        self.gateway = gateway

    def make_payment(self):
        return self.gateway.process_payment('using net banking')
