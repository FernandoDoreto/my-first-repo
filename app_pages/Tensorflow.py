import streamlit as st
import pandas as pd
import numpy as np


from app_pages.Sklearn import TrainTestSplit,PredictAndEvaluate

def PageTensorflow(df,TARGET):

    if st.button("Fit a Deep Learning Model and Predict"):

        X_train, X_test,y_train, y_test = TrainTestSplit(df,TARGET)


        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        X_train = scaler.fit_transform(X_train)
        X_test =  scaler.transform(X_test)
        
        model = CreateTensorflowModel(n_features=X_train.shape[1])        
        model.fit(X_train, y_train, epochs=100, batch_size=32)

        st.write("### Your Deep Learning model was created and fit to the Train Set!")
        model.summary()
        st.write("---")

        PredictAndEvaluate(model,X_test,y_test,flag="TF")

 


def CreateTensorflowModel(n_features): 
            from tensorflow.keras.models import Sequential
            from tensorflow.keras.layers import Dense
            model = Sequential()
            model.add(Dense(25, activation='relu', input_shape=(n_features,)))
            model.add(Dense(10, activation='relu'))
            model.add(Dense(15, activation='softmax'))
            model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            return model

