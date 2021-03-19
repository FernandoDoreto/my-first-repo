import streamlit as st
import pandas as pd
import numpy as np


from app_pages.Sklearn import TrainTestSplit,PredictAndEvaluate

def PageTensorflow(df,TARGET):
    X_train, X_test,y_train, y_test = TrainTestSplit(df,TARGET)

    ml_pipeline = CreateFitTensorflowPipeline(X_train,y_train)




def CreateModelTensorflow():
        
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    model = Sequential()
    model.add(Dense(3,activation='relu'))
    model.add(Dense(3,activation='relu'))
    model.add(Dense(1))
    model.compile(optmizer='adam',loss='mse')
    return model

def CreateFitTensorflowPipeline(X_train,y_train):


    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import MinMaxScaler

    model = CreateModelTensorflow()


    ml_pipeline = Pipeline([       
        ("feat_scaling",MinMaxScaler()),
        ("model", model)
    ])

    ml_pipeline.fit(X_train,y_train,epochs=20)

    st.write("### Your ML Pipeline was created and fit to the Train Set!")
    st.code(ml_pipeline)
    st.write("---")

    return ml_pipeline

