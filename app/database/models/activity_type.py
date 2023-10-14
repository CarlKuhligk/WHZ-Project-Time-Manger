from ._base import *


class ActivityType(Base, Default):
    name = Column(String(64), unique=True, nullable=False)
    salary = Column(Integer, nullable=False)
