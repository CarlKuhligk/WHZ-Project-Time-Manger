from ._base import *
from enum import Enum as PyEnum
from .employee import Employee
from .activity_type import ActivityType


class ActivityCategory(PyEnum):
    TESTING = "testing"
    DOCUMENTATION = "documentation"
    CONSULTATION = "consultation"
    DEVELOPMENT = "development"


class Activity(Base, Default):
    project_id = Column(Integer, ForeignKey("Project.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("Employee.id"), nullable=False)
    type_id = Column(Integer, ForeignKey("ActivityType.id"), nullable=False)
    category = Column(Enum(ActivityCategory), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    _Employee: Mapped[Employee] = relationship(
        Employee, uselist=False, single_parent=True
    )
    _ActivityType: Mapped[ActivityType] = relationship(
        ActivityType, uselist=False, single_parent=True
    )
