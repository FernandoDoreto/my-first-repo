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
    st.write("This is PageSklearn")

    X_train, X_test,y_train, y_test = train_test_split(
                                        df.drop([TARGET],axis=1),
                                        df[TARGET],
                                        test_size=0.2,
                                        random_state=0,
                                        stratify=df[TARGET]
                                        )

    ml_pipeline = CreateFitPipeline(X_train,y_train)


def PredictAndEvaluate(ml_pipeline,X,y):

    Pred = ml_pipeline.predict(X_test)
    st.write(Pred_Xtest)

    st.code(classification_report(y_test, Pred_Xtest))

    st.code(pd.DataFrame(confusion_matrix(y_pred_adj,y_test),
                    columns=['pred_neg', 'pred_pos'], 
                    index=['neg', 'pos']))


def CreateFitPipeline(X_train,y_train):

    ml_pipeline = Pipeline([       
        ("feat_selection",SelectFromModel(DecisionTreeClassifier())),
        ("scaler",StandardScaler()),
        ("model", DecisionTreeClassifier())
    ])

    ml_pipeline.fit(X_train,y_train)
    return ml_pipeline