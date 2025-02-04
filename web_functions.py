import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st


@st.cache_data()

def load_data():
    df=pd.read_csv('diabetes.csv')
    X = df[['HbA1c_level','Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
    y = df['Outcome']

    return df, X, y


@st.cache_data()

def train_model(X,y):
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, #Increases the amount of pruning, which reduces overfitting. 
        class_weight=None, #This parameter allows you to assign different weights to classes
        criterion='entropy', #This parameter determines the function to measure the quality of a split.
        max_depth=4, #A deeper tree can model more complex patterns but may lead to overfitting
        max_features=None, #This parameter controls the number of features to consider when looking for the best split
        max_leaf_nodes=None, #This parameter limits the maximum number of leaf nodes in the tree. Setting this parameter can help control overfitting.
        min_impurity_decrease=0.0, #If the impurity decrease from a split is less than this value, the split will not be performed.
        min_samples_leaf=1, #A smaller value allows the tree to create more leaves, which can lead to overfitting.
        min_samples_split=2, #If a node has fewer samples than this value, it will not be split
        min_weight_fraction_leaf=0.0, #This parameter controls the minimum weighted fraction of the total sum of weights 
        random_state=42, #Setting it to an integer ensures that the results are reproducible.
        splitter='best' #This parameter controls the strategy used to choose the split at each node.
        )
    
    model.fit(X,y)

    score = model.score(X,y)

    return model, score

def predict(X, y, features):
    model, score = train_model(X, y)
    
    # Reshape the features correctly
    features = np.array(features).reshape(1, -1)  # Reshape to (1, n_features)
    
    prediction = model.predict(features)
    
    return prediction, score


