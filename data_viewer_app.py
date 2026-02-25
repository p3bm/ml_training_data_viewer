import pandas as pd
import streamlit as st
import seaborn as sns

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

st.write(f"Total number of values: {len(data[data_column])}")
st.write(f"Data type: {data[data_column].dtypes}")
st.write(f"Number of missing values: {data[data_column].isna()}")

st.write(f"Overview of data in {data_column}:")
st.write(data[data_column].describe())

if st.toggle(f"View value counts for {data_column}"):
    st.write(data[data_column].value_counts())

if st.toggle(f"View histogram for {data_column}"):
    try:
        data[data_column].hist()
        st.pyplot()
    except ValueError as e:
        st.error(e)
        st.error(f"Unable to generate histogram for {data_column}")

if st.toggle(f"View box plot for {data_column}"):
    try:
        data[[data_column]].boxplot()
        st.pyplot()
    except ValueError as e:
        st.error(e)
        st.error(f"Unable to generate box plot for {data_column}")

# Multiple column box plots
st.divider()
st.subheader("Multiple Column Box Plots")

columns_to_boxplot = st.multiselect("Select multiple columns to create box plots for", options = data.columns)

if columns_to_boxplot:
    try:
        data[columns_to_boxplot].boxplot()
        st.pyplot()
    except ValueError as e:
        st.error(e)
        st.error(f"Unable to generate box plot(s) for one or more selected columns")

# Pairwise plots
st.divider()
st.subheader("Pair Plots")

columns_to_pairplot = st.multiselect("Select multiple columns to create pair plots for", options = data.columns)

if columns_to_pairplot:
    try:
        sns.pairplot(data[columns_to_pairplot])
        st.pyplot()
    except Exception as e:
        st.error(e)
        st.error(f"Unable to generate pair plot(s) for one or more selected columns")
