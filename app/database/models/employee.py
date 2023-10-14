from ._base import *
from enum import Enum as PyEnum


class Department(PyEnum):
    MARKETING = "marketing"
    PRODUKTION = "production"
    DEVELOPMENT = "development"
    MANAGEMENT = "management"
    SERVICE = "service"


class Employee(Base, Default):
    name = Column(String(64), unique=True, nullable=False) # unique name for testing
    salary = Column(Integer, nullable=False)
    department = Column(Enum(Department), nullable=False)

