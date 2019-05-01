import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
dbname = os.environ.get('DBNAME')
connect_string = "mysql+pymysql://{username}:{password}@{host}/{dbname}?charset=utf8mb4".format(username=username,
                                                                                                password=password,
                                                                                                host=host,
                                                                                                dbname=dbname)

engine = create_engine(connect_string, convert_unicode=True, echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()
