import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier 

from sklearn.metrics import classification_report,confusion_matrix
	

def PageSklearn(df,TARGET):
    if st.button("Fit a ML Pipeline and Predict"):

        X_train, X_test,y_train, y_test = train_test_split(
                                            df.drop([TARGET],axis=1),
                                            df[TARGET],
                                            test_size=0.2,
                                            random_state=0,
                                            stratify=df[TARGET]
                                            )

        ml_pipeline = CreateFitPipeline(X_train,y_train)

        st.write("### Predictions and Evaluation on Test Set")
        PredictAndEvaluate(ml_pipeline,X_test,y_test)


def PredictAndEvaluate(ml_pipeline,X,y):

    Pred = ml_pipeline.predict(X)
    st.write("#### Predictions")
    st.write(Pred)

    st.write("#### Classification Report")
    st.code(classification_report(y, Pred))

    st.write("#### Confusion Matrix")
    ClassMap = ['0','1','2']

    st.code(pd.DataFrame(confusion_matrix(Pred,y),
                columns=[ ["Actual " + sub for sub in ClassMap] ], 
                index = [ ["Prediction " + sub for sub in ClassMap ]]
                # index=['Prediction 0', 'Prediction 1']
                ))


def CreateFitPipeline(X_train,y_train):

    ml_pipeline = Pipeline([       
        ("feat_selection",SelectFromModel(DecisionTreeClassifier())),
        ("feat_scaling",StandardScaler()),
        ("model", DecisionTreeClassifier())
    ])

    ml_pipeline.fit(X_train,y_train)

    st.write("#### Your ML Pipeline was created and fit!")
    st.code(ml_pipeline)
    st.write("---")

    return ml_pipeline