from ._base import *
from .activity_category import ActivityCategory


class ProjectCategory(Base, Default):
    name = Column(String(64), unique=True, nullable=False)
