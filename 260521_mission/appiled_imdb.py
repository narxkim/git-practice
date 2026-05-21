import streamlit as st, pandas as pd, plotly.express as px

@st.cache_data
def load_imdb():
    df = pd.read_csv('./imdb_top_1000.csv')
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    return df

imdb = load_imdb().copy()

with st.sidebar:
    min_rating = st.slider("최소 평점", 7.0, 9.5, 7.6, step=0.1)
    year_range = st.slider("개봉 연도", 1920, 2020, (2000, 2020))


filtered = imdb[
    (imdb['IMDB_Rating'] >= min_rating) &
    (imdb['Released_Year'] >= year_range[0]) &
    (imdb['Released_Year'] <= year_range[1]) 
]

tab1, tab2 = st.tabs(["평점 분포", "투표 수 vs 평점"])
# A1. metric 2개 + 평점 히스토그램
with tab1:
    col1, col2 = st.columns(2)

    col1.metric("영화 수", len(filtered))
    col2.metric("평균 평점", round(filtered['IMDB_Rating'].mean(), 2))

    fig = px.histogram(
        filtered,
        x="IMDB_Rating",
        nbins=20,
        title='평점 분포',
        template="simple_white"
    )
    st.plotly_chart(fig, width='stretch')


# A2. 투표 수 vs 평점 scatter 탭 추가 (hover_name='Series_Title')
with tab2:
    fig = px.scatter(
        filtered,
        x="No_of_Votes",
        y="IMDB_Rating",
        hover_name="Series_Title",
        title="투표 수 vs 평점",
        template="simple_white",
        labels={"No_of_Votes":'투표 수', 'IMDB_Rating' : '평점'},
        opacity=0.8
    )
    st.plotly_chart(fig, width='stretch')
