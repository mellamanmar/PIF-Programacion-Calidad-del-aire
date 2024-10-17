from pydantic import BaseModel,Field
from typing import Optional

class Pollutants(BaseModel):
    id: Optional[int]= None
    Cp: float= Field( description="Concentración medida del contaminante")
    PCalto: int= Field(description="Punto de corte mayor o igual al contaminante")
    PCbajo: int= Field( description="Punto de corte menor o igual al contaminante")
    Ialto: int= Field( description="Valor del ICA correspondiente al 𝑃𝐶𝑎𝑙𝑡𝑜")
    Ibajo: int= Field(description="Valor del ICA correspondiente al 𝑃𝐶bajo")

    class Config:
        schema_extra = {
            "example":{
                'id' : 1,
                'Cp' : 209.07,
                'PCalto' : 677,
                'PCbajo' : 190,
                'Ialto' : 150,
                'Ibajo' : 101
            }
        }