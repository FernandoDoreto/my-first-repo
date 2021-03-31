import numpy as np
import pingouin as pg
import streamlit as st

np.random.seed(123)
mean, cov, n = [4, 5], [(1, .6), (.6, 1)], 30
x, y = np.random.multivariate_normal(mean, cov, n).T

st.write(x,y)
