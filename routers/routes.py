from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models import Pollutants, Air_Quality
from services.Pollutants import Services as ServicePollutants
from schemas.Pollutants import Pollutants as SchemaPollutants
from schemas.Air_Quality import Air_Quality as SchemaAirQuality

pullutants_router= APIRouter()


@pullutants_router.get('/pollutants', tags=['pollutants'], status_code=200)
def get_pollutants():
    db= Session()
    result= ServicePollutants(db).get_pollutants()
    return JSONResponse(content= jsonable_encoder(result), status_code= 200)

@pullutants_router.post ('/createpollutants', tags= ['createpollutants'], status_code=201,response_model=dict)
def create_pollutants(data:SchemaPollutants):
    db = Session()
    ServicePollutants(db).agregate_data(data)
    return JSONResponse(content={"message":"Added product successfully", "status_code":201})