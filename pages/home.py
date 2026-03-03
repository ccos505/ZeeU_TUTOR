import streamlit as st

def render_home():
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <h1>ZeeU TUTOR</h1>
            <p>เตรียมสอบเข้า ม.1 & ม.4 แบบมืออาชีพ</p>
        </div>
    </div>
    """, unsafe_allow_html=True)