<h1>Quora Question Pair Analysis using NLP</h1>

## Project Overview:

The objective of this project is to build a model using NLP techniques to determine whether pairs of questions on Quora have the same intent or are semantically similar. The project will involve data collection, preprocessing, feature engineering, model building, and evaluation to create a reliable question similarity classifier.

Challenges:

Converting text data to numerical format is the most laborious task i have tried various techniques and finally i came up with countvectorizer it may sound most frequent method but trust me using this method i was able to achieve 80% accuracy i have also added some features as well you can check their discription on notebook folder.

## Objectives:

* Data Collection: Gather question pairs dataset from Quora, ensuring it includes pairs labeled as duplicates and non-duplicates for supervised learning.

* Data Preprocessing: Clean and preprocess the text data by removing HTML tags, special characters, and tokenizing text. Perform normalization and handle missing values if present.

* Feature Engineering: Extract relevant features such as word embeddings (Word2Vec, GloVe), TF-IDF vectors, or sentence embeddings to represent the questions.

* Model Building: Utilize machine learning algorithms (e.g., Logistic Regression, Random Forest, XGBoost) or deep learning models (e.g., Siamese networks, LSTM) to train a classifier to predict question similarity.

* Fine-tuning and Optimization: Fine-tune the model parameters, experiment with different embeddings or architectures, and optimize to improve the model's performance.

## Steps To Run the Project

Step1: First clone the repository using
```sh
git clone https://github.com/harshayr/Quora-Question-Pairs.git
```

Step2: go into current working directory 
```sh
cd Quora-Question-Pairs
 
```

Step3: Install prerequisites by pasting below command to your terminal
```sh
pip install -r requirment.txt
```

Step4: Run streamlit file using terminal or command promt
```sh
streamlit run app.py
```