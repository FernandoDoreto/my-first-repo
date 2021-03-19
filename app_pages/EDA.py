import streamlit as st
from scr.eda import PlotPairplot, Plot3D, HeatmapCorrelation

def PageEDA(df):

    st.write("---")
    st.write("#### Pair Plot")
    PlotPairplot(df,"Species")

    st.write("---")
    st.write("#### 3D Plot")
    Plot3D(df,"Species")

    st.write("---")
    st.write("#### Heatmap")
    HeatmapCorrelation(df)