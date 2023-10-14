from ._base import *


class Customer(Base, Default):
    name = Column(String(64), unique=True, nullable=False) # unique name for testing
