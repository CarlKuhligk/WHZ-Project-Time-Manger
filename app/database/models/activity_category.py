from ._base import *


class ActivityCategory(Base, Default):
    name = Column(String(32))
    rate = Column(Integer)
