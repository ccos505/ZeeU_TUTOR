import streamlit as st

st.title("ZeeU TUTOR")
st.subheader("Math Tutoring")

st.write("รับสอนพิเศษคณิตศาสตร์ เน้นเข้าใจระยะยาว")

name = st.text_input("ชื่อผู้สมัคร")
phone = st.text_input("เบอร์โทร")

if st.button("สมัครเรียน"):
    st.success("ส่งข้อมูลเรียบร้อยแล้ว")
