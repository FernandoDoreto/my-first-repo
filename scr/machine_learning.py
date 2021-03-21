import pandas as pd
import streamlit as st



def TrainTestSplit(df,TARGET):
    from sklearn.model_selection import train_test_split

    X_train, X_test,y_train, y_test = train_test_split(
                                        df.drop([TARGET],axis=1),
                                        df[TARGET],
                                        test_size=0.2,
                                        random_state=0,
                                        stratify=df[TARGET]
                                        )
    st.write(" * Train Set", pd.concat([X_train,y_train], axis=1))
    st.write("* Test Set", pd.concat([X_test,y_test], axis=1))
    st.write("---")

    return X_train, X_test,y_train, y_test


def EvaluatePredictions(Pred, y):

    from sklearn.metrics import classification_report,confusion_matrix  

    st.write("#### Classification Report")
    st.code(classification_report(y, Pred))

    st.write("#### Confusion Matrix")
    ClassMap = ['0','1','2']

    st.code(pd.DataFrame(confusion_matrix(Pred,y),
                columns=[ ["Actual " + sub for sub in ClassMap] ], 
                index = [ ["Prediction " + sub for sub in ClassMap ]]
                # index=['Prediction 0', 'Prediction 1']
                ))

