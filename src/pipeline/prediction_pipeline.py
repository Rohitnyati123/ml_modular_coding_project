from src.constants import *
from src.logger import logging
from src.exception import CustomException
import os, sys
# from src.config.configuration import *
from src.config.configuration import PREPROCESSING_OBJ_PATH,MODEL_FILE_PATH
from src.utils import load_model
import pandas as pd
from src.components.data_transformation import Feature_Engineering



class PredictionPipeline:
    def __init__(self) -> None:
        pass

    def predict_d(self,features):
        try:
            preprocessor_path= PREPROCESSING_OBJ_PATH
            model_path=MODEL_FILE_PATH

            preprocessor=load_model(preprocessor_path) #preprocessor_path

            model=load_model(model_path)
            
            data_scaled=preprocessor.transform(features)

            # pred=model.predict([[2.82912340 4.09473134 1.19265145 3.47338763 4.61305554 2.31277217 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 2.11840500 0.00000000 7.22755906 2.38980125 0.00000000 0.00000000 0.00000000 0.00000000]])

            # pred=model.predict([[2, 4, 1, 3, 4, 2, 0, 0, 0, 0, 0, 0, 2, 0, 7, 2, 0, 0, 0, 0]])
            pred=model.predict(data_scaled)
            
            return pred
        except Exception as e:
            logging.info("Error occured in prediction pipeline")
            raise CustomException(e,sys)
        
"""categorical_columns = ['Type_of_order','Type_of_vehicle','Festival','City']
            ordinal_encoder = ['Road_traffic_density', 'Weather_conditions']
            numerical_column=['Delivery_person_Age','Delivery_person_Ratings','Vehicle_condition',
                              'multiple_deliveries','distance']"""

class CustomData:
    def __init__(self,
                Delivery_person_Age: int,
                Delivery_person_Ratings:float,
                Weather_conditions:str,
                Road_traffic_density:str,
                Vehicle_condition:int,
                multiple_deliveries:int,
                distance:float,
                Type_of_order:str,
                Type_of_vehicle:str,
                Festival:str,
                City:str) -> None:
        self.Delivery_person_Age=Delivery_person_Age
        self.Delivery_person_Ratings=Delivery_person_Ratings
        self.Weather_conditions=Weather_conditions
        self.Road_traffic_density=Road_traffic_density
        self.Vehicle_condition=Vehicle_condition
        self.multiple_deliveries=multiple_deliveries
        self.distance=distance
        self.Type_of_order=Type_of_order
        self.Type_of_vehicle=Type_of_vehicle
        self.Festival=Festival
        self.City=City

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Delivery_person_Age':[self.Delivery_person_Age],
                'Delivery_person_Ratings':[self.Delivery_person_Ratings],
                'Weather_conditions':[self.Weather_conditions],
                'Road_traffic_density':[self.Road_traffic_density],
                'Vehicle_condition':[self.Vehicle_condition],
                'multiple_deliveries':[self.multiple_deliveries],
                'distance':[self.distance],
                'Type_of_order':[self.Type_of_order],
                'Type_of_vehicle':[self.Type_of_vehicle],
                'Festival':[self.Festival],
                'City':[self.City]


            }
            
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("DataFrame gatherd")
            
            return df
        except Exception as e:
            logging.info("Exception occured in Custom data")
            raise CustomException(e,sys)