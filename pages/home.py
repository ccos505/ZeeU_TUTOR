import streamlit as st
from pathlib import Path
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

BASE_DIR = Path(__file__).resolve().parent
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
        st.image(ASSETS_DIR / "teacher1.jpg", use_container_width=True)
        st.markdown("""
        ### ครูนก  

        **การศึกษา:** ปริญญาตรี คณิตศาสตร์  
        **ประสบการณ์:** 20 ปี  
        **ความเชี่ยวชาญ:** คณิตศาสตร์
        """)

    with col2:
        st.image(ASSETS_DIR / "teacher2.jpg", use_container_width=True)
        st.markdown("""
        ### ครูพี่คอส  

        **การศึกษา:** ปริญญาตรี เกียรตินิยม จุฬาลงกรณ์มหาวิทยาลัย สาขา คณิตศาสตร์ประกันภัย  
        **ประสบการณ์:** 4 ปี  
        **ความเชี่ยวชาญ:** โอลิมปิกวิชาการ สาขาคณิตศาสตร์, TPAT1, ONET
        """)

    with col3:
        st.image(ASSETS_DIR / "teacher3.jpg", use_container_width=True)
        st.markdown("""
        ### ครูพี่คิม  

        **การศึกษา:** ปริญญาตรี เกียรตินิยม ครุศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย  
        **ประสบการณ์:** 2 ปี  
        **ความเชี่ยวชาญ:** ปูพื้นฐานแน่น เข้าใจง่าย
        """)