import datetime
from typing import List, Union
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
    TIMESTAMP,
    text,
    Date,
    TIME,
    inspect,
    FLOAT,
    Enum,
    and_,
    DateTime
)
from sqlalchemy.orm import (
    Mapped,
    relationship,
    Session,
    declared_attr,
    as_declarative,
)


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__

    id = Column(Integer, primary_key=True, autoincrement=True)


class Default:
    def as_dict(self) -> dict:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
