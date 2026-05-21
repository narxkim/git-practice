import streamlit as st ,pandas as pd, plotly.express as px

# 타이타닉 데이터
@st.cache_data
def load_titanic():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    return pd.read_csv(url)

df = load_titanic().copy()
df['Age'] = df['Age'].fillna(df['Age'].median())

st.title('타이타닉 필터 대시보드')

# 사이드바 위젯 4종
with st.sidebar:
    st.header("필터")
    st.divider() # 구분선
    pclass_options = st.multiselect("객실 등급", [1,2,3], default=[1,2,3])
    gender = st.selectbox("성별", ["전체", "male", "female"])
    age_range = st.slider("나이 범위", 0, 80, (0,80))
    survived_only = st.checkbox("생존자만 보기")

filtered = df[df["Pclass"].isin(pclass_options)]
filtered = filtered[(filtered["Age"] >= age_range[0]) & (filtered["Age"] < age_range[1])]

if gender != "전체":
    filtered = filtered[filtered['Sex'] == gender]

if survived_only:
    filtered = filtered[filtered['Survived'] == 1]

st.write(f'결과 : {len(filtered)}명')
st.dataframe(filtered.head(10))

st.divider()

# metric 3개
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('선택된 승객', len(filtered))

with col2:
    st.metric("생존자", filtered["Survived"].sum())

with col3:
    rate = f"{filtered['Survived'].mean()*100:.1f}%" if len(filtered) > 0 else "N/A" 
    st.metric("생존률", rate)

st.divider()

# tab 차트, 데이터로 분리
tab1, tab2, tab3 = st.tabs(["나이분포 ", "등급별 생존", "데이터"])
with tab1:
    fig = px.histogram(
        filtered, 
        x='Age', 
        nbins=20, 
        title='나이 분포',
        template='simple_white')
    st.plotly_chart(fig, width='stretch')

with tab2:
    surv = filtered.groupby("Pclass")["Survived"].mean().reset_index()
    fig2 = px.bar(
        surv, x="Pclass", y="Survived", title="등급별 생존율", template="simple_white",
        labels={"Pclass":"객실 등급", "Survived": '생존율'}
    )
    st.plotly_chart(fig2, width='stretch')
    st.caption('1등급 생존율이 가장 높다.')

with tab3:
    st.dataframe(
        filtered[["Name", "Survived", "Pclass", "Sex", "Age", "Fare"]], hide_index=True
    )
