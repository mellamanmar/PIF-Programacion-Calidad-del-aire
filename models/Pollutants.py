from sqlalchemy import *
from config.database import Base

class Pollutants(Base):
    __tablename__ ="Contaminantes"

    id = Column(Integer, primary_key= True) 
    Cp= Column(Double)      ## Concentración medida del contaminante
    PCalto= Column(Double)  ## Punto de corte mayor o igual al contaminante
    PCbajo= Column(Double)  ## Punto de corte menor o igual al contaminante
    Ialto= Column(Double)   ## Valor del ICA correspondiente al 𝑃𝐶𝑎𝑙𝑡𝑜
    Ibajo= Column(Double)   ## Valor del ICA correspondiente al 𝑃𝐶bajo

    




