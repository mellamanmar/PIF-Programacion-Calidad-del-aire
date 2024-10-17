from pydantic import BaseModel,Field
from typing import Optional

class Air_Quality(BaseModel):
    id: Optional[int]= None
    ICAp: float= Field(description="Calidad del aire")

    class Config:
        schema_extra = {
            "example":{
                'id' : 1,
                'ICAp' : 102.91,
            }
        }