from sqlalchemy import *
from config.database import Base


class Supplies(Base):
    __tablename__= "Air Quality"

    id= Column(Integer, primary_key=True)
    quality= Column(Double)
    pollutants_hour = Column (DateTime, ForeignKey("Pollutants.time_out"))
    