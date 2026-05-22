import streamlit as st
import plotly.express as px

st.title("Marketing Campaign Dashboard")
st.divider()
st.markdown("<br>", unsafe_allow_html=True)

# app.py에서 공유한 필터 데이터 가져오기
if "filtered_data" in st.session_state:
    filtered = st.session_state["filtered_data"]
else:
    st.warning("데이터를 불러올 수 없습니다. 메인 홈을 확인해 주세요.")
    st.stop()

# 주요 성과 지표(KPI)
st.subheader("주요 성과 지표(KPI)")
col1, col2, col3 = st.columns(3)

if not filtered.empty:
    avg_roi = filtered["ROI"].mean()
    total_clicks = filtered["Clicks"].sum()
    avg_conversion = filtered["Conversion_Rate"].mean() * 100

    col1.metric("평균 ROI", f"{avg_roi:.2f} x")
    col2.metric("총 클릭 수 (Clicks)", f"{total_clicks: ,}회")
    col3.metric("평균 전환율 (Conversion)", f"{avg_conversion:.2f} %")

    st.divider()

    # 타겟 오디언스별 선호 채널 분석
    st.subheader("Target Audience 별 선호 채널 분석 (유입 기준)")
    st.divider()
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("#### **오디언스 X 채널 별 총 클릭 수**")
        pivot_clicks = filtered.pivot_table(
            index="Target_Audience",
            columns="Channel_Used",
            values="Clicks",
            aggfunc="sum",
        )
        st.dataframe(pivot_clicks.style.format("{:,.0f}"), use_container_width=True)

    with chart_col2:
        st.markdown("#### **타겟 오디언스별 총 클릭 수**")
        audience_clicks_mk_df = (
            filtered.groupby("Target_Audience", as_index=False)["Clicks"]
            .sum()
            .sort_values(by="Clicks", ascending=False)
        )
        fig = px.bar(
            audience_clicks_mk_df,
            x="Target_Audience",
            y="Clicks",
            labels={"Target_Audience": "타겟 오디언스", "Clicks": "총 클릭 수"},
            color="Clicks",
            color_continuous_scale="Purples",
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("선택한 필터 조건에 맞는 데이터가 없습니다.")
