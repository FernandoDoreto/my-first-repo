import streamlit as st
import pandas as pd
import numpy as np
from scr.machine_learning import TrainTestSplit, EvaluatePredictions



def PageSklearn(df,TARGET):
    
    if st.button("Fit a ML Pipeline with Sklearn and Predict"):

        X_train, X_test,y_train, y_test = TrainTestSplit(df,TARGET)
        ml_pipeline = CreateFitSklearnPipeline(X_train,y_train)

        st.write("### Predictions and Evaluation on Test Set")
        Prediction = PredictionSklearn(ml_pipeline,X_test)
        EvaluatePredictions(Pred=Prediction, y=y_test)




def CreateFitSklearnPipeline(X_train,y_train):

    from sklearn.pipeline import Pipeline
    from sklearn.feature_selection import SelectFromModel
    from sklearn.preprocessing import StandardScaler
    from sklearn.tree import DecisionTreeClassifier 

    ml_pipeline = Pipeline([       
        ("feat_selection",SelectFromModel(DecisionTreeClassifier())),
        ("feat_scaling",StandardScaler()),
        ("model", DecisionTreeClassifier())
    ])

    ml_pipeline.fit(X_train,y_train)

    st.write("### Your ML Pipeline was created and fit to the Train Set!")
    st.code(ml_pipeline)
    st.write("---")

    return ml_pipeline



def PredictionSklearn(ml_pipeline,X):

    Prediction = ml_pipeline.predict(X)
    st.write("#### Predictions")
    st.write(Prediction)
    
    return Prediction 

