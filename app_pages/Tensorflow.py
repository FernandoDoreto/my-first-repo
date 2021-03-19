import streamlit as st
import pandas as pd
import numpy as np


from app_pages.Sklearn import TrainTestSplit,PredictAndEvaluate

def PageTensorflow(df,TARGET):

    X_train, X_test,y_train, y_test = TrainTestSplit(df,TARGET)


    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test =  scaler.transform(X_test)

    
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    model = Sequential()
    model.add(Dense(10, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=150, batch_size=32)

    st.write("### Your ML Pipeline was created and fit to the Train Set!")
    st.write("---")


    



    PredictAndEvaluate(model,X_test,y_test,flag="TF")

 


