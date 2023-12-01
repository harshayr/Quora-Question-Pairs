import os 
import pandas as pd
import sys
import numpy as np
from tqdm import tqdm

from source.exception import CustomException
from source.logger import logging
from source.utils import preprocess,save_file
from dataclasses import dataclass




@dataclass
class IngestDataConfig:
    data_path = os.path.join("artifacts", "sample_data.csv")

class IngestData:

    try:

        def __init__(self):
            self.IngestDataConfig = IngestDataConfig()
        
        def load_data(self):
            df = pd.read_csv("/Users/harshalrajput/Desktop/nlp_mlops/Notebook/data/quora_duplicate_questions.tsv", sep = '\t')
            df_0 = df[df["is_duplicate"]==0][:25000]
            df_1 = df[df["is_duplicate"]==1][:25000]
            new_df = pd.concat([df_0,df_1]).sample(frac=1, random_state=42)
            new_df['question1'] = new_df['question1'].apply(preprocess)
            new_df['question2'] = new_df['question2'].apply(preprocess)

            save_file(self.IngestDataConfig.data_path,new_df)
            logging.info("Data preprocessing complete")

            return new_df
        
    except Exception as e:
        raise CustomException(e,sys)

    









