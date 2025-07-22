import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')




st.sidebar.title("India's Data Visualization")

selected_state = st.sidebar.selectbox("Select a state", list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_map(df, lat='Latitude', lon='Longitude', size=primary, color=secondary, size_max=35, zoom=3,
                                map_style="carto-positron", width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, user_container_width=True)
    else:
        st.text('Size represents primary parameter')
        st.text('Color represents secondary parameter')
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_map(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, size_max=35, zoom=3,
                             map_style="carto-positron", width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, user_container_width=True)