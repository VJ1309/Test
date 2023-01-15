import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu




st.markdown(
    """
    <style>
    .main {
    background-color: #eaeae1;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title('Collector Efficiency')
#st.text('In this project I look into the transactions of taxis in NYC. ...')
selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#a8b5b4"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#2358eb"},
            },
        )

        
#st.set_page_config(page_title='Collector Efficiency')
#st.title("Collector's Efficiency 📈")
#st.subheader('Feed me with your Excel file')


#selected_year = st.sidebar.selectbox('Year', ('2020','2021','2022'))

if selected == 'Home':
    st.markdown('''
         #### Percentage of members with goals asdadasdasdasdasda
        #### asfasfdasfasf
        ''', unsafe_allow_html=True)
elif selected == 'Projects':
    st.sidebar.header('User Input Features')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, parse_dates=["Action Assigned Date"])
        df["Action Assigned Date Year"] = df["Action Assigned Date"].dt.year
        startdate = ('2020', '2021', '2022')
        st.write(df.info())
    

    

    
    
    
    #startdate = ('2022-01-01')
    
    
        df['CompanyCode'] = df['CompanyCode'].astype(str)
    #df['Action Assigned Date'] = pd.to_datetime(df['Action Assigned Date'])
    #selected_year = st.sidebar.selectbox('Year', list(reversed(df['Action Assigned Date'].dt.year.unique())))

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
elif selected == 'Contact':
    st.write("Varun")
