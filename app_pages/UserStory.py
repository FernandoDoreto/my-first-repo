import streamlit as st

def PageUserStory(df):
    st.write("### User Story")
    st.write(
        f"* As a Data Analyst from Botanic Garden, you are requested by Special Flower division to "
        f" develop a system capable to distinguish among **3 distinct Iris flowers**. \n "
        f"* We will create an App to inform what is the **flower species** "
        f"based on **sepal and petal measurements**. "
        f"It is a 3-class, single-label, classification model: 0 (Setosa ), 1 (Versicolour) and 2 (Virginica). \n"
        f"* Our ideal outcome is to help Special Flowers botanics to speed up their diagnosis " 
        f"during their next field mission at XYZ forest.")