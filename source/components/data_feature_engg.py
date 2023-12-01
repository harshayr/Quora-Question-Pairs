import os 
import pandas as pd
import sys
import numpy as np
from nltk.corpus import stopwords

from source.utils import common_words,total_words,fetch_token_features, fetch_length_features, fetch_fuzzy_features, save_file

from source.exception import CustomException
from source.logger import logging
from dataclasses import dataclass

@dataclass
class FeatureEnggConfig:
    new_feature_data = os.path.join("artifacts",'new_features_data.csv')


class FeatureEngg:
    
    def __init__(self):
        self.feature_config = FeatureEnggConfig()


    def feature_engg(self, new_df):
        try:
            # new_df = pd.read_csv(self.data_path
            new_df['q1_len'] = new_df['question1'].str.len() 
            new_df['q2_len'] = new_df['question2'].str.len()
            new_df['q1_num_words'] = new_df['question1'].apply(lambda row: len(row.split(" ")))
            new_df['q2_num_words'] = new_df['question2'].apply(lambda row: len(row.split(" ")))
            new_df['word_common'] = new_df.apply(common_words, axis=1)
            new_df['word_total'] = new_df.apply(total_words, axis=1)
            new_df['word_share'] = round(new_df['word_common']/new_df['word_total'],2)

            logging.info("Basic features created")

            token_features = new_df.apply(fetch_token_features, axis=1)

            new_df["cwc_min"]       = list(map(lambda x: x[0], token_features))
            new_df["cwc_max"]       = list(map(lambda x: x[1], token_features))
            new_df["csc_min"]       = list(map(lambda x: x[2], token_features))
            new_df["csc_max"]       = list(map(lambda x: x[3], token_features))
            new_df["ctc_min"]       = list(map(lambda x: x[4], token_features))
            new_df["ctc_max"]       = list(map(lambda x: x[5], token_features))
            new_df["last_word_eq"]  = list(map(lambda x: x[6], token_features))
            new_df["first_word_eq"] = list(map(lambda x: x[7], token_features))

            logging.info("Tokenize features done")

            length_features = new_df.apply(fetch_length_features, axis=1)
            new_df['longest_substr_ratio'] = list(map(lambda x: x[0], length_features))

            fuzzy_features = new_df.apply(fetch_fuzzy_features, axis=1)

            new_df['fuzz_ratio'] = list(map(lambda x: x[0], fuzzy_features))
            new_df['fuzz_partial_ratio'] = list(map(lambda x: x[1], fuzzy_features))
            new_df['token_sort_ratio'] = list(map(lambda x: x[2], fuzzy_features))
            new_df['token_set_ratio'] = list(map(lambda x: x[3], fuzzy_features))

            logging.info("Fuzzy features done")

            save_file(self.feature_config.new_feature_data, new_df)

            return new_df
        except Exception as e:
            raise CustomException(e , sys)
        
        














