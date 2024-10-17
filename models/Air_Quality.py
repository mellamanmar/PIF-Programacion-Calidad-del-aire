from sqlalchemy import *
from config.database import Base


class Air_Quality(Base):
    __tablename__= "Calidad del aire"

    id= Column(Integer, primary_key=True)
    ICAp= Column(Double)
    