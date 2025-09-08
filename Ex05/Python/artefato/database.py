from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("mysql+mysqlconnector://root:root@localhost/projetojava", echo=False)
Session = sessionmaker(bind=engine)
