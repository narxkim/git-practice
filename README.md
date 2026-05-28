# Python 기반 데이터 분석 및 데이터 시각화를 위한 Streamlit 웹 대시보드

## 과정 소개
본 저장소는  
「Python 기반 데이터 분석 및 데이터 시각화를 위한 Streamlit 웹 대시보드」강의 학습 내용을 정리하기 위한 저장소입니다.

Python을 활용한 데이터 분석 및 시각화 과정과 Streamlit 기반 웹 대시보드 구현 내용을 학습 및 실습 중심으로 기록합니다.

---

## 학습 목표
- Python 데이터 분석 기초 학습
- Pandas 기반 데이터 처리 및 전처리
- 데이터 시각화 구현
- Streamlit 기반 웹 대시보드 개발
- 데이터 기반 인사이트 도출
- Git & GitHub 기반 학습 관리

---

## 학습 기술 스택

<details>
<summary>Language</summary>

- Python

</details>



<details>
<summary>Data Analysis</summary>

- NumPy
- Pandas

</details>



<details>
<summary>Visualization</summary>

- Matplotlib
- Plotly

</details>



<details>
<summary>Dashboard</summary>

- Streamlit

</details>



<details>
<summary>Development Environment</summary>

- VS Code
- Jupyter Notebook
- Git
- GitHub

</details>

## 학습 내용

<details>
<summary>2026-05-18 | CLI & Git 기초</summary>

### CLI 명령어
```bash
pwd          # 현재 위치 확인
cd           # 폴더 이동
mkdir        # 폴더 생성
ls           # 파일 목록 확인
ls -a        # 숨김 파일 포함 전체 보기
cd ..        # 상위 폴더 이동
```

### Git 기본 개념
- Working Directory
- Staging Area
- Repository

### Git 명령어
```bash
git init
git status
git add .
git add <파일명>
git commit
git log --oneline
git switch -c <브랜치명>
git push -u origin main
git push
```

</details>



<details>
<summary>2026-05-19 | uv · NumPy · Pandas 기초</summary>

### Python 환경 관리
- uv
- 가상환경(.venv)
- pyproject.toml
- uv.lock

### NumPy
- ndarray
- 벡터 연산
- 배열 인덱싱
- shape / dtype / ndim

### Pandas
- DataFrame 탐색
- head / info / describe
- loc / iloc
- 조건 필터링
- 결측치 처리
- groupby / agg 집계

### 실습
- Titanic 데이터 분석
- 생존율 분석
- 결측치 처리
- 그룹별 통계 분석

### Git 실습
```bash
git add .
git commit -m "feat: pandas 기초 실습 완료"
git push
```

</details>


<details>
<summary>2026-05-20 | EDA · matplotlib · plotly 데이터 시각화</summary>

### EDA (탐색적 데이터 분석)
- EDA 개념 및 데이터 탐색 흐름
- 데이터 분포 · 이상치 · 변수 관계 분석
- Anscombe’s Quartet 사례 분석
- 시각화 기반 데이터 해석

### 차트 선택 기준
- 히스토그램 (분포)
- 막대그래프 (비교)
- 산점도 (관계)
- 박스플롯 (이상치)
- 파이차트 (구성)
- 꺾은선그래프 (추세)

### matplotlib
- fig / ax 객체 구조
- plt.subplots()
- hist / bar / scatter / boxplot / pie
- tight_layout()
- savefig()
- 한글 폰트 설정

### plotly express
- px.histogram()
- px.scatter()
- px.line()
- px.bar()
- hover_name / hover_data
- marginal 옵션
- fig.write_html()

### 데이터 전처리
- pd.to_numeric(errors='coerce')
- 문자열 숫자 정제
- astype(str)
- str.split() / explode()
- 결측치 및 이상치 처리

### 실습
- Titanic 데이터 시각화
- IMDB Top 1000 분석
- 서울 아파트 실거래 데이터 분석
- 월별 거래 추이 시각화
- 구별 평균 거래가격 분석

### Git 실습
```bash
git add .
git commit -m "feat: 시각화 실습 완료"
git push
````

</details>


<details>
<summary>2026-05-21 | Streamlit · 인터랙티브 대시보드</summary>

### Streamlit 기초
- Streamlit 개념 및 실행 구조
- Python 기반 웹 앱 개발
- top-to-bottom rerun 모델
- 데이터 대시보드 프로토타이핑

### 환경 설정
- uv init
- uv add streamlit watchdog
- uv run streamlit run app.py
- watchdog 활용

### 기본 출력
- st.title()
- st.header()
- st.subheader()
- st.write()
- st.markdown()
- st.text()

### 위젯
- text_input
- selectbox
- slider
- checkbox
- multiselect
- button

### 사이드바
- st.sidebar
- 사용자 입력 필터 구성
- 데이터 조건 필터링
- 대시보드 레이아웃 분리

### 데이터 출력 및 시각화
- st.dataframe()
- st.metric()
- st.plotly_chart()
- Plotly 인터랙티브 차트 연동

### 레이아웃 구성
- st.columns()
- st.tabs()
- st.caption()
- st.divider()

### 캐시 최적화
- @st.cache_data
- rerun 성능 최적화
- .copy() 활용
- CachedObjectMutationWarning 대응

### 실습
- Titanic 필터 대시보드 제작
- IMDB 대시보드 제작
- 서울 아파트 대시보드 제작
- Plotly 기반 인터랙티브 차트 구성
- 사이드바 기반 데이터 필터링

### Git 실습
```bash
git add .
git commit -m "feat: Streamlit 대시보드 실습 완료"
git push
````

</details>


<details>
<summary>2026-05-26 | 머신러닝 개요 · 지도학습 파이프라인 · k-NN</summary>

### 머신러닝 개요

* AI · ML · DL 관계 이해
* 머신러닝과 전통 프로그래밍 차이
* 데이터 기반 학습 개념
* 패턴 학습 기반 예측 구조

### 머신러닝 학습 유형

* 지도학습 (Supervised Learning)
* 비지도학습 (Unsupervised Learning)
* 강화학습 (Reinforcement Learning)

### 지도학습

* 분류(Classification)
* 회귀(Regression)
* Feature / Label 개념
* Sample 개념
* 입력(X)과 정답(y) 구조 이해

### 비지도학습

* Clustering
* PCA(차원 축소)
* 이상 탐지(Anomaly Detection)

### 지도학습 파이프라인

* 데이터 수집
* 특성 선택
* train / test 분리
* 모델 학습
* 예측
* 평가

### train_test_split

* train / test 데이터 분리 이유
* 일반화(Generalization)
* 데이터 누수(Data Leakage)
* random_state
* stratify

### k-NN 알고리즘

* 거리 기반 분류 알고리즘
* KNeighborsClassifier
* k 값에 따른 성능 변화
* 다수결 기반 예측
* 최근접 이웃 개념

### scikit-learn 기본 패턴

```python
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()

kn.fit(X_train, y_train)

kn.predict(X_new)

kn.score(X_test, y_test)
```

### 데이터 시각화

* matplotlib scatter plot
* 도미 · 빙어 산점도 시각화
* 클래스 분포 시각화

### 실습

* 생선 데이터 분류
* 도미 / 빙어 분류 모델 구현
* train_test_split 적용
* k 값 비교 실습
* score 1.0 문제 분석
* 타이타닉 문제 정의 워크숍

### 주요 개념 정리

* Feature
* Label
* Training Set
* Test Set
* Generalization
* Classification
* Regression

### 오류 해결

* ModuleNotFoundError
* ValueError
* list index out of range
* random_state 재현성 문제
* matplotlib 그래프 출력 문제

### Git 실습

```bash
git add .
git commit -m "feat: 머신러닝 기초 및 k-NN 실습 완료"
git push
```

</details>


