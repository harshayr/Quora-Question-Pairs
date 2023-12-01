import pandas as pd
import sys
import numpy as np
import os

from source.exception import CustomException
from source.logger import logging
from dataclasses import dataclass

from sklearn.feature_extraction.text import CountVectorizer
from source.utils import save_file
from dataclasses import dataclass

@dataclass
class TransformDataConfig:
    cv = CountVectorizer(max_features=3000)


class TransformData:

    def __init__(self):
        self.countvector = TransformDataConfig()

    def transform_data(self,new_df):

        try:
            logging.info("data transformation start")
            # new_df = pd.read_csv(data_path)

            ques_df = new_df[['question1','question2']]
            questions = list(ques_df['question1']) + list(ques_df['question2'])
            # cv = CountVectorizer(max_features=3000)
            q1_arr, q2_arr = np.vsplit(self.countvector.cv.fit_transform(questions).toarray(),2)

            temp_df1 = pd.DataFrame(q1_arr, index= ques_df.index)
            temp_df2 = pd.DataFrame(q2_arr, index= ques_df.index)
            temp_df = pd.concat([temp_df1, temp_df2], axis=1)

            df = new_df.drop(columns=['id','qid1','qid2','question1','question2'])

            final_df = pd.concat([df, temp_df], axis=1)

            logging.info("data transformation finish")

            return final_df
        except Exception as e:
            raise CustomException(e,sys)
   





