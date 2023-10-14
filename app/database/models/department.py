from ._base import *


class Department(Base, Default):
    name = Column(String(64), unique=True, nullable=False)  # unique name for testing
