from sql.base import Session
from sql.tables import User


def get_user_annotation(annotation):
    session = Session()
    return session.query(User).filter(User.annotation == annotation).all()


def get_users():
    session = Session()
    return session.query(User).all()
