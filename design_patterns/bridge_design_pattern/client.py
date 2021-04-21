from design_patterns.bridge_design_pattern.payment_gateway import AxisPaymentGateway, DbsPaymentGateway
from design_patterns.bridge_design_pattern.payment_method import CardPaymentMethod, NetBankingPaymentMethod

gateway = AxisPaymentGateway()
payment_method = CardPaymentMethod(gateway)
out = payment_method.make_payment()
print(out)

gateway = DbsPaymentGateway()
payment_method = NetBankingPaymentMethod(gateway)
out = payment_method.make_payment()
print(out)
