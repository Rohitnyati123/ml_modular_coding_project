from src.constants import *
from src.config.configuration import *
import os,sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
import pickle
from src.utils import load_model
from sklearn.pipeline import Pipeline

PREDICTION_FOLDER="batch_prediction"
PREDICTION_CSV="prediction_csv"
PREDICTION_FILE="prediction.csv"
FEATURE_ENG_FOLDER="feature_eng"

ROOT_DIR=os.getcwd()
BATCH_PREDICTION=os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_CSV)
FEATURE_ENG=os.path.join(ROOT_DIR,PREDICTION_FOLDER,FEATURE_ENG_FOLDER)

class batch_prediction:
    def __init__(self,input_file_path,
                 model_file_path,
                 transformer_file_path,
                 feature_eng_file_path) -> None:
        self.input_file_path=input_file_path
        self.model_file_path=model_file_path
        self.transformer_file_path=transformer_file_path
        self.feature_eng_file_path=feature_eng_file_path

    
    def start_batch_prediction(self):
        try:
            # load the feature engg pipeline path
            with open(self.feature_eng_file_path,'rb') as f:
                feature_pipeline=pickle.load(f)

            # load the data transformation pipeline path
            with open(self.feature_eng_file_path,'rb') as f:
                processor=pickle.load(f)

            # load the model separately
                
            model = load_model(file_path=self.model_file_path)

            # create a feature eng pipeline
            feature_eng_pipeline=Pipeline([
                ("feature_engineering",feature_pipeline)
            ])

            df=pd.read_csv(self.input_file_path)

            df.to_csv("df_zomato_delivery_prediction.csv")

            # Apply a feature engineering pipeline steps

            df=feature_eng_pipeline.transform(df)

            df.to_csv("feature_engineering.csv")

            FEATURE_ENGINEERING_PATH=FEATURE_ENG

            os.makedirs(FEATURE_ENGINEERING_PATH,exist_ok=True)

            file_path=os.path.join(FEATURE_ENGINEERING_PATH,'batch_feature_eng.csv')

            df.to_csv(file_path,index=False)

            # time taking column

            df=df.drop('Time_taken (min)',axis=1)

            df.to_csv("time_takend_dropped.csv")

            transform_data= processor.transform(df)

            file_path=os.path.join(FEATURE_ENGINEERING_PATH,"processor.csv")

            predictions=model.predict(transform_data)

            df_prediction=pd.DataFrame(predictions,columns=['prediction'])

            BATCH_PREDICTION_PATH=BATCH_PREDICTION
            os.makedirs(BATCH_PREDICTION,exist_ok=True)
            csv_path=os.path.join(BATCH_PREDICTION_PATH,'output.csv')

            df_prediction.to_csv(csv_path,index=False)
            logging.info("Batch Prediction Done")

        except Exception as e:
            raise CustomException(e,sys)

