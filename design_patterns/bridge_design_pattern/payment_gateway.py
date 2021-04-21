from abc import abstractmethod


class IPaymentGateway:
    @abstractmethod
    def process_payment(self, payment_method):
        pass


class AxisPaymentGateway(IPaymentGateway):
    def __init__(self):
        pass

    def process_payment(self, payment_method):
        return f"Doing payment using Axis gateway with {payment_method}"


class DbsPaymentGateway(IPaymentGateway):
    def __init__(self):
        pass

    def process_payment(self, payment_method):
        return f"Doing payment using DBS gateway with {payment_method}"
