
from source.components.data_feature_engg import FeatureEngg
from source.components.data_transform import TransformData
from source.components.model_train import ModelTrain
from source.components.data_ingestion import IngestData



if __name__ ==  "__main__":
    obj_1 = IngestData()
    new_df = obj_1.load_data()
    obj_2 = FeatureEngg()
    new_df = obj_2.feature_engg(new_df)
    obj_3 = TransformData()
    final_df = obj_3.transform_data(new_df)
    obj_4 = ModelTrain()
    obj_4.train_model(final_df)


    