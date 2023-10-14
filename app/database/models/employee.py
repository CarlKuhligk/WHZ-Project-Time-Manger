from ._base import *
from .department import Department


class Employee(Base, Default):
    name = Column(String(64), unique=True, nullable=False)  # unique name for testing
    salary = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey("Department.id"), nullable=False)

    _Department: Mapped[Department] = relationship(
        Department, uselist=False, single_parent=True
    )
