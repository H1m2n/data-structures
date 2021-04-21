from design_patterns.abstract_factory.i_processor import IProcessor
from design_patterns.abstract_factory.product_specifactions import Processor


class I7Processor(IProcessor):
    def __init__(self):
        pass

    def get_processor(self):
        return Processor.I7.name
