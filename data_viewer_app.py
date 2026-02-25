import pandas as pd
import streamlit as st

# Create app
st.image('./catsci-logo.svg')
st.title("ML Training Data Viewer")

# Load data
datafile = st.file_uploader(label="Please upload a suitable CSV file", type="csv")
if not datafile:
    st.stop()
data = pd.read_csv(datafile, sep=",")

# Basic info
st.header(datafile.name)
st.write(f"Number of rows: {data.shape[0]}")
st.write(f"Number of columns: {data.shape[1]}")
st.table(data.describe())
st.dataframe(data)

# Single column information
st.divider()
data_column = st.selectbox(
    label = "Select a column to analyse",
    options = data.columns
)

if data_column:
    st.write(data[data_column].head(10))
    st.write(data[data_column].describe())
    st.write(f"Most commmon values for {data_column}:")
    st.write(data[data_column].value_counts())
    #st.pyplot(data[data_column].hist())
    #st.pylot(data[[data_column]].boxplot())

# Pairwise plots
# Multiple box plots
