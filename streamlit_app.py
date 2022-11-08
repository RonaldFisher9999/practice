import streamlit as st
import joblib
import numpy as np

# 헤드라인
st.write("# 보험료 예측")

# 첫번째 행
r1_col1, r1_col2, r1_col3 = st.columns(3)

age = r1_col1.number_input("age (between 1~100)", step=1, value=20, min_value=1, max_value=100)

height = r1_col2.number_input("height (cm)", value=170)
weight = r1_col2.number_input("weight (kg)", value=60)
bmi = (height/100)**2 / weight

children = r1_col3.number_input("children", step=1, value=0, min_value=0)

# 두번째 행
r2_col1, r2_col2, r2_col3 = st.columns(3)

smoker_option = r2_col1.radio(label='smoker', options=("yes", "no"))
if smoker_option == "yes" :
    smoker = 1
else :
    smoker = 0

sex_option = r2_col2.radio(label='sex', options=("male", "female"))
if sex_option == "male" :
    sex = 1
else :
    sex = 0

region_option = ('southwest', 'southeast', 'northwest', 'northeast')
region = r2_col3.selectbox("region", region_option)
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