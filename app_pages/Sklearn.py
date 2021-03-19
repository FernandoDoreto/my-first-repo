import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier 

def PageSklearn(df,TARGET):
    st.write("This is PageSklearn")

    X_train, X_test,y_train, y_test = train_test_split(
                                        df.drop([TARGET],axis=1),
                                        df[TARGET],
                                        test_size=-.2,
                                        random_state=0,
                                        stratify=df[TARGET]
                                        )

    st.write(X_train,y_train)

     



    # ml_pipeline = Pipeline(
    # [       
    #     ("feat_selection",SelectFromModel(DecisionTreeClassifier())),
    #     ("scaler",StandardScaler()),
    #     ("model", DecisionTreeClassifier)
    # ])