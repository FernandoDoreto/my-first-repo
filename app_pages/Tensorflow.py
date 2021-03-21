import streamlit as st
import pandas as pd
import numpy as np
from scr.machine_learning import TrainTestSplit, EvaluatePredictions

def PageTensorflow(df,TARGET):

    if st.button("Fit a Deep Learning Model and Predict"):

        X_train, X_test,y_train, y_test = TrainTestSplit(df,TARGET)
        model, X_test = CreateFitTensorflow(X_train,y_train,X_test)

        st.write("### Predictions and Evaluation on Test Set")
        Prediction = PredictionTensorflow(model,X_test)
        EvaluatePredictions(Pred=Prediction, y=y_test)
     

 

def CreateFitTensorflow(X_train,y_train,X_test):

    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test =  scaler.transform(X_test)

    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense
    model = Sequential()
    model.add(Dense(25, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(15, activation='softmax'))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])       
    model.fit(X_train, y_train, epochs=100, batch_size=32)

    st.write("### Your Deep Learning model was created and fit to the Train Set!")
    model.summary()
    st.write("---")

    return model, X_test



def PredictionTensorflow(model,X):

    Prediction = model.predict_classes(X)
    st.write("#### Predictions")
    st.write(Prediction)
    
    return Prediction 