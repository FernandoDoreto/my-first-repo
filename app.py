import streamlit as st
from app_pages.UserStory import PageUserStory

def main():

    MenuOptions = [
        'User Story',
        'EDA',
        'Sklearn',
        'Tensorflow',
        ]
    page = st.sidebar.selectbox("Main Menu",MenuOptions,index=0)
    
    if page == MenuOptions[0]: PageUserStory()
    # elif page == MenuOptions[1]: Page_EDA()   
    # elif page == MenuOptions[2]: Page_ML_Pipeline()
    # elif page == MenuOptions[3]: ML_Evaluation_and_Explanation()

if __name__ == '__main__': main()