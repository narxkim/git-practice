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

if not filtered.empty:
    st.subheader("Target Audience 별 투자 대비 수익률 분석")
    st.divider()
    roi_col1, roi_col2 = st.columns(2)

    st.divider()
    with roi_col1:
        st.markdown("#### 오디언스 X 채널 별 평균 ROI")
        pivot_roi = filtered.pivot_table(
            index="Target_Audience",
            columns="Channel_Used",
            values="ROI",
            aggfunc="mean",
        )
        st.dataframe(pivot_roi.style.format("{:.2f} x"), use_container_width=True)

    with roi_col2:
        st.markdown("##### 타겟 오디언스별 전체 평균 ROI 순위")
        audience_roi_df = (
            filtered.groupby("Target_Audience", as_index=False)["ROI"]
            .mean()
            .sort_values(by="ROI", ascending=False)
        )
        fig_roi = px.bar(
            audience_roi_df,
            x="Target_Audience",
            y="ROI",
            labels={"Target_Audience": "타겟 오디언스", "ROI": "평균 ROI (배)"},
            color="ROI",
            color_continuous_scale="Teal",
        )
        fig_roi.update_layout(plot_bgcolor="rgba(0,0,0,0)", coloraxis_showscale=False)
        st.plotly_chart(fig_roi, use_container_width=True)
else:
    st.warning("선택한 필터 조건에 맞는 데이터가 없습니다.")
