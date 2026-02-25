import pandas as pd
import streamlit as st

# Create app
st.image('./catsci-logo (1).svg', width=300)
st.title("ML Training Data Viewer")

# Load data
datafile = st.file_uploader(label="Please upload a suitable CSV file", type="csv")
if not datafile:
    st.stop()
data = pd.read_csv(datafile, sep=",")

# Basic info
st.header(datafile.name.replace(".csv",""))
st.write(f"Number of rows: {data.shape[0]}")
st.write(f"Number of columns: {data.shape[1]}")
st.subheader("Dataframe Overview")
st.table(data.describe())

if st.toggle("View entire dataframe"):
    st.dataframe(data)

# Select a column
# show fist X values, get data type, no. of missing values, median and mean if approrpriate, most common values
st.divider()
st.subheader("Single Column Information")
data_column = st.selectbox(
    label = "Select a column to analyse",
    options = data.columns
)

st.write(data[data_column].describe())

if st.toggle(f"View value counts for {data_column}"):
    st.write(data[data_column].value_counts())

st.pyplot(data[data_column].hist())
st.pyplot(data[[data_column]].boxplot())

# Single column plots
# histogram
# box plot(s)

# Pairwise plots
