import streamlit as st
from app_pages.UserStory import PageUserStory
from app_pages.EDA import PageEDA
from app_pages.Sklearn import PageSklearn
from app_pages.Tensorflow import PageTensorflow

from scr.data_management import LoadIrisDataset

def main():

    df = LoadIrisDataset()

    MenuOptions = [
        'User Story',
        'EDA',
        'Sklearn',
        'Tensorflow',
        ]
    page = st.sidebar.radio("Main Menu",MenuOptions,index=0)
    
    if page == MenuOptions[0]: PageUserStory(df)
    elif page == MenuOptions[1]: PageEDA(df)   
    elif page == MenuOptions[2]: PageSklearn(df,TARGET="Species")
    elif page == MenuOptions[3]: PageTensorflow(df,TARGET="Species")

if __name__ == '__main__': main()