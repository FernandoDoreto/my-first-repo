import streamlit as st
from scr.data_management import LoadIrisDataset
df = LoadIrisDataset()

st.write(
    df.dtypes ,
    df.describe()
    )






def PandasProfiling(df):

    from pandas_profiling import ProfileReport
    from streamlit_pandas_profiling import st_profile_report

    pr = ProfileReport(df, explorative=True,minimal=True)
    st_profile_report(pr)

PandasProfiling(df)



### missing data
def MissingDataMap(df,plotMap):
    import pandas as pd
    import matplotlib as plt
    import seaborn as sns
    import streamlit as st
    st.write("#### Missing Data Map")
    null = df.isna().sum()#/len(df)
    st.write(type(null))
    # null = null[null > 0].sort_values(ascending=False)
    nullDf = pd.concat(
        [null,round(null/len(df)*100,2)], axis=1)
    nullDf.columns = ['Absolute Number','Percentage (%) of dataset']

    st.write("* Raw dataset shape: ",df.shape)
    st.write("* Data Type")
    st.code(df.dtypes)
    st.write("* Frequency of missing data: ")
    st.code(nullDf)

    if plotMap:
        fig = plt.figure()
        sns.heatmap(df.isnull(), cbar=False)
        st.pyplot(fig,clear_figure=True)

# MissingDataMap(df,1)