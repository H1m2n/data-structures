from design_patterns.abstract_factory.i_brand import IBrand
from design_patterns.abstract_factory.product_specifactions import Brand


class Dell(IBrand):
    def __init__(self):
        pass

    def get_brand(self):
        return Brand.dell.name
