from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sql.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    annotation = Column(String)
    name = Column(String)
    country = Column(String)
    hobby_one = Column(String)
    hobby_two = Column(String)
    hobby_three = Column(String)
    hobby_four = Column(String)
    hobby_five = Column(String)
    favorite_os = Column(String)
    language_one = Column(String)
    language_two = Column(String)
    language_three = Column(String)
    language_four = Column(String)
    language_five = Column(String)