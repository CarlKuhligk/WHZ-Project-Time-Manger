from ._base import *
from .customer import Customer
from .activity import Activity
from .project_category import ProjectCategory


class Project(Base, Default):
    name = Column(String(64), unique=True, nullable=False)  # unique name for testing
    project_category_id = Column(Integer, ForeignKey("ProjectCategory.id"))
    customer_id = Column(Integer, ForeignKey("Customer.id"))

    _Customer: Mapped[List[Customer]] = relationship(
        Customer, uselist=False, single_parent=True
    )
    _Activities: Mapped[List[Activity]] = relationship(
        Activity, uselist=True, single_parent=True
    )
    _Category: Mapped[List[ProjectCategory]] = relationship(
        ProjectCategory, uselist=True, single_parent=True
    )
