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


