import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Top 50 films", layout= "wide")
st.title("Top Films of all time")

@st.cache_data
def load():
    conn= sqlite3.connect("Movies.db")
    df= pd.read_sql_query("select * from Top_50",conn)
    conn.close()

    df['Year'] =pd.to_numeric(df['Year'],errors= 'coerce')
    df['Average Rank']= pd.to_numeric(df['Average Rank'],errors= 'coerce')

    return df

df= load()

st.sidebar.header("Filter here")
min_year, max_year= int(df['Year'].min()), int(df['Year'].max())
year_range= st.sidebar.slider("Select the year range", min_year, max_year, (min_year,max_year))

filtered_df= df[df['Year'].between(year_range[0], year_range[1])]

col1, col2, col3 = st.columns(3)
col1.metric("Total Movies Displayed", len(filtered_df))
col2.metric("Oldest Movie Year", int(filtered_df['Year'].min()) if not filtered_df.empty else "N/A")
col3.metric("Newest Movie Year", int(filtered_df['Year'].max()) if not filtered_df.empty else "N/A")

st.markdown("---")
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Distribution of Movies Across Decades")
    filtered_df['Decade'] = (filtered_df['Year'] // 10) * 10
    decade_counts = filtered_df['Decade'].value_counts().reset_index()
    decade_counts.columns = ['Decade', 'Count']
    
    fig_bar = px.bar(
        decade_counts, 
        x='Decade', 
        y='Count', 
        labels={'Decade': 'Decade (s)', 'Count': 'Number of Films'},
        text_auto=True
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with right_col:
    st.subheader("Rank vs. Release Year")
    fig_scatter = px.scatter(
        filtered_df, 
        x='Year', 
        y='Average Rank', 
        hover_name='Film',
        size_max=10
    )
    fig_scatter.update_yaxes(autorange="reversed")  # Rank 1 at the top
    st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("Top Films Data Table")
st.dataframe(filtered_df, use_container_width=True)