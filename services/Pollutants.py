from models.Pollutants import Pollutants as PollutantsModel
from models.Air_Quality import Air_Quality as AirQualityModel

class Services ():
    def __init__(self,db):
        self.db = db

    def get_pollutants(self):
        data= self.db.query(PollutantsModel).all()
        return data
    
    def get_pollutants_for_id(self,id:int):
        result= self.db.query(PollutantsModel).filter(PollutantsModel.id == id).first()
        return result
    
    def agregate_data(self, data:PollutantsModel, quality:AirQualityModel):
        new_data = PollutantsModel(
            Cp= data.Cp,
            PCalto= data.PCalto,
            PCbajo= data.PCbajo,
            Ialto= data.Ialto,
            Ibajo= data.Ibajo
        )
        self.db.add(new_data)
        quality = ((new_data.Ialto-new_data.Ibajo)/(new_data.Ialto-new_data.Ibajo))*(new_data.Cp-new_data.PCbajo)+new_data.Ibajo
        self.db.add(quality)
        self.db.commit()
        return
    
    def get_quaality(self):
        data= self.db.query(AirQualityModel).all()
        return data
    
    def get_quality_for_id(self,id:int):
        result= self.db.query(AirQualityModel).filter(AirQualityModel.id == id).first()
        return result


    def delete_product(self, id: int):
        self.db.query(AirQualityModel).filter(AirQualityModel.id == id).delete()
        self.db.commit()
        return