import streamlit as st
import pandas as pd
import numpy as np

a=[1,2,3,4,5,6,7,8]
n=np.array(a)

nd = n.reshape((2,4))
dictionary={
    "name":"anuj",
    "age":39,
    "city":"pune"
}

df=pd.read_csv("resources//tran.csv")
st.dataframe(df)
