import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title='Collector Efficiency')
st.title("Collector's Efficiency 📈")
st.subheader('Feed me with your Excel file')

st.sidebar.header('User Input Features')
#selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    #st.dataframe(df)
    df['CompanyCode'] = df['CompanyCode'].astype(str)
    df['Action Assigned Date'] = pd.to_datetime(df['Action Assigned Date'])
selected_year = st.sidebar.selectbox('Year', list(reversed(df['Action Assigned Date'].dt.year.unique())))

groupby_column = st.sidebar.selectbox(
        'What would you like to analyse?',
        ('CompanyCode', 'Collector Name', 'Customer Name', 'Action Assigned Date'),
    )

     # -- GROUP DATAFRAME
output_columns = ['Amount']
df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()
   
    # -- PLOT DATAFRAME

fig = px.bar(
        df_grouped,
        x=groupby_column,
        y='Amount',
        template='plotly_white',
        title=f'<b>Amount by {groupby_column}</b>'
        )
st.plotly_chart(fig)


uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)

#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
  #df = pd.read_csv(uploaded_file)
 # st.write(df)

#function = ["O2C","Make"]

#O2C = pd.read_csv("D:\Python\Datasets\O2C.csv")


#species_option = st.selectbox('Select Columns',('sepal_length','sepal_width','petal_length','petal_width','species'))
#data = explore_data(my_dataset)
#if species_option == 'sepal_length':
#	st.write(data['sepal_length'])
#elif species_option == 'sepal_width':
#	st.write(data['sepal_width'])
