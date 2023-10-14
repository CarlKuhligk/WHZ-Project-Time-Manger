from ._base import *
from enum import Enum as PyEnum
from .customer import Customer
from .activity import Activity


class ProjectCategory(PyEnum):
    RESEARCH = "research"
    DATABASE = "database"



class Project(Base, Default):
    name = Column(String(64), unique=True, nullable=False)  # unique name for testing
    category = Column(Enum(ProjectCategory), nullable=False)
    customer_id = Column(Integer, ForeignKey("Customer.id"))

    _Customer: Mapped[List[Customer]] = relationship(Customer, uselist=False, single_parent=True)
    _Activities: Mapped[List[Activity]] = relationship(
        Activity, uselist=True, single_parent=True
    )
