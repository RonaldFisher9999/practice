import streamlit as st
import joblib
import numpy as np

# 헤드라인
st.write("# 보험료 예측")

# 첫번째 행
r1_col1, r1_col2, r1_col3 = st.columns(3)

age = r1_col1.number_input("나이 (최대 100까지)", step=1, value=20, max_value=100)

height = r1_col2.number_input("키 (cm)", step=None, value=170)
weight = r1_col2.number_input("몸무게 (kg)", step=None, value=60)
bmi = (height/100)**2 / weight

children = r1_col3.number_input("자녀 수", step=1, value=0, min_value=0)

# 두번째 행
r2_col1, r2_col2, r2_col3 = st.columns(3)

smoker_option = r2_col1.radio(label='흡연 여부', options=("예", "아니오"))
if smoker_option == "예" :
    smoker = 1
else :
    smoker = 0

sex_option = r2_col2.radio(label='성별', options=("남성", "여성"))
if sex_option == "male" :
    sex = 1
else :
    sex = 0

region_option = ('서남', '동남', '서북', '동북')
region = r2_col3.selectbox("거주 지역", region_option)
is_southwest = region_option[0] == region
is_southeast = region_option[1] == region
is_northwest = region_option[2] == region

# 예측 버튼
predict_button = st.button("예측")

st.write("---")

# 예측 결과
if predict_button:
    model = joblib.load('first_model.pkl')

    pred = model.predict(np.array([[age, bmi, children, smoker * 1,
        sex * 1, is_northwest * 1, is_southeast * 1, is_southwest * 1]]))

    st.metric("예측 보험료", pred[0])