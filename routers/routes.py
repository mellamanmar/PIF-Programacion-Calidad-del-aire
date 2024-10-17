from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models import Pollutants, Air_Quality

