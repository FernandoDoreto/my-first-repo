import streamlit as st
from scr.eda import PlotPairplot,Plot3D

def PageEDA(df):

    st.write("---")
    st.write("#### Matplotlib Example")

    st.write("---")

    st.write("#### Seaborn Example")
    PlotPairplot(df,"Species")

    st.write("---")
    st.write("#### Plotly Example")
    Plot3D(df,"Species")