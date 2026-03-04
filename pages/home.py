import streamlit as st
from pathlib import Path
import os
from utils.image_utils import get_base64


BASE_DIR = Path(__file__).resolve().parent

# print(f"BASE_DIR: {BASE_DIR}")
# print(f"ASSETS_DIR: {BASE_DIR.parent / 'assets'}")
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(f"BASE_DIR: {BASE_DIR}")
ASSETS_DIR = BASE_DIR.parent / "assets"

def render_home():
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <h1>ZeeU TUTOR</h1>
            <p>เตรียมสอบเข้า ม.1 & ม.4 แบบมืออาชีพ</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
def render_teachers():

    st.markdown("## 👩‍🏫 คุณครูของเรา")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        t1 = get_base64(ASSETS_DIR / "hero1.jpg")

        st.markdown(f"""
            <img src="data:image/jpeg;base64,{t1}" 
                style="width:100%; border-radius:12px; margin-bottom:15px;">

            ### ครูนก  

            **การศึกษา:** ปริญญาตรี คณิตศาสตร์  
            **ประสบการณ์:** 20 ปี  
            **ความเชี่ยวชาญ:** คณิตศาสตร์
        """, unsafe_allow_html=True)


    with col2:
        t2 = get_base64(ASSETS_DIR / "hero2.jpg")

        st.markdown(f"""
            <img src="data:image/jpeg;base64,{t2}" 
                style="width:100%; border-radius:12px; margin-bottom:15px;">

            ### ครูพี่คอส  

            **การศึกษา:** ปริญญาตรี เกียรตินิยม จุฬาลงกรณ์มหาวิทยาลัย สาขา คณิตศาสตร์ประกันภัย  
            **ประสบการณ์:** 4 ปี  
            **ความเชี่ยวชาญ:** โอลิมปิกวิชาการ สาขาคณิตศาสตร์, TPAT1, ONET
        """, unsafe_allow_html=True)
        
    with col3:
        t3 = get_base64(ASSETS_DIR / "teacher3.jpg")

        st.markdown(f"""
            <img src="data:image/jpeg;base64,{t3}" 
                style="width:100%; border-radius:12px;">

            ### ครูพี่คิม  

            **การศึกษา:** ปริญญาตรี เกียรตินิยม ครุศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย  
            **ประสบการณ์:** 2 ปี  
            **ความเชี่ยวชาญ:** ปูพื้นฐานแน่น เข้าใจง่าย  
        """, unsafe_allow_html=True)