from sqlalchemy import *
from config.database import Base

class Pollutants(Base):
    __tablename__ ="Contaminantes"

    id = Column(Integer, primary_key= True) 
    particles= Column(Double)   ## Concentracion de las partículas contaminantes
    time_in= Column(DateTime)   ## Hora de medición inicial
    time_out= Column(DateTime)  ## Hora de medición final



