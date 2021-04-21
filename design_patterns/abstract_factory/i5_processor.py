from design_patterns.abstract_factory.i_processor import IProcessor
from design_patterns.abstract_factory.product_specifactions import Processor


class I5Processor(IProcessor):
    def __init__(self):
        pass

    def get_processor(self):
        return Processor.I5.name
