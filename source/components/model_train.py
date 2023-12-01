from source.exception import CustomException
from source.logger import logging
from source.utils import evaluate_model,save_file

import os 
import pandas as pd
import sys
import numpy as np
import pickle

from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class ModelTrainConfig:
    model_path = os.path.join("artifacts", "model.pkl")

class ModelTrain:

    def __init__(self):
        self.model_path = ModelTrainConfig()

    def train_model(self,data):
        try:

            y = data["is_duplicate"]
            x = data.drop(["is_duplicate"], axis = 1)
            
            X_train,X_test,y_train,y_test = train_test_split(x.values,y.values,test_size=0.2)


            models ={
            "Random Forest": RandomForestClassifier(),
            "XGBClassifier": XGBClassifier(),

             } 
    
            params = {

                            "Random Forest": {
                                # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],

            #                     'max_features':['sqrt','log2',None],
                                'n_estimators': [8, 16, 32, 64, 128, 256]
                            },
                
                            "XGBRegressor": {
                                'learning_rate': [.1, .01, .05, .001],
                                'n_estimators': [8, 16, 32, 64, 128, 256]
                            }
            }

            model_report,param = evaluate_model(X_train,y_train,X_test,y_test, models, params)

            best_model_score = max(sorted(list(model_report.values())))
            # to get best scored model name
            best_model_name = list(model_report.keys())[(list(model_report.values())).index(best_model_score)]
            best_param = list(param.keys())[(list(param.values())).index(best_model_score)]
            best_model = models[best_model_name]
            save_file(
                file_path = self.model_path.model_path,
                obj = best_model
            )
            logging.info('Best : {}, using {}'.format(best_model_name,best_param))

        except Exception as e:
            raise CustomException(e,sys)
