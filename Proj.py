import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
st.header("This is Nizar")
st.write("hello world")
data = {
    'Name':['NIzar','sabari','nishanth'],
    'Age':[20,28,48]

}
df=pd.DataFrame(data)
st.dataframe(df)
name=st.text_input("Enter your name")
st.write(f"Hello!,{name}!")