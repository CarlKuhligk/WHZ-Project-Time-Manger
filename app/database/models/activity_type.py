from ._base import *
from .activity_category import ActivityCategory


class ActivityType(Base, Default):
    name = Column(String(64), unique=True, nullable=False)

    activity_category_id = Column(
        Integer, ForeignKey("ActivityCategory.id"), nullable=False
    )

    _ActivityCategory: Mapped[ActivityCategory] = relationship(
        ActivityCategory, uselist=False, single_parent=True
    )
