import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title='Collector Efficiency')
st.title("Collector's Efficiency 📈")
st.subheader('Feed me with your Excel file')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.markdown('---')
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    df['CompanyCode'] = df['CompanyCode'].astype(str)
    groupby_column = st.selectbox(
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


#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
  #df = pd.read_csv(uploaded_file)
 # st.write(df)

#function = ["O2C","Make"]

#O2C = pd.read_csv("D:\Python\Datasets\O2C.csv")



#st.sidebar.title("Functions")

#choice = st.sidebar.selectbox("Select Functional Area",function)
#if choice == "O2C":
#		st.write(O2C)

#species_option = st.selectbox('Select Columns',('sepal_length','sepal_width','petal_length','petal_width','species'))
#data = explore_data(my_dataset)
#if species_option == 'sepal_length':
#	st.write(data['sepal_length'])
#elif species_option == 'sepal_width':
#	st.write(data['sepal_width'])