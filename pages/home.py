import streamlit as st
from pathlib import Path
from utils.image_utils import get_base64


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

    t1 = get_base64(ASSETS_DIR / "teacher1.jpg")
    t2 = get_base64(ASSETS_DIR / "teacher2.jpg")
    t3 = get_base64(ASSETS_DIR / "teacher3.jpg")

    st.markdown("""
    <div class="teacher-section">
        <div class="teacher-title">👩‍🏫 คุณครูของเรา</div>
        <div class="teacher-grid">
    """, unsafe_allow_html=True)

    # Card 1
    st.markdown(f"""
        <div class="teacher-card">
            <img src="data:image/jpeg;base64,{t1}" class="teacher-img">
            <div class="teacher-content">
                <div class="teacher-name">ครูนก</div>
                <div class="teacher-detail"><b>การศึกษา:</b> ปริญญาตรี คณิตศาสตร์</div>
                <div class="teacher-detail"><b>ประสบการณ์:</b> 20 ปี</div>
                <div class="teacher-detail"><b>ความเชี่ยวชาญ:</b> คณิตศาสตร์</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Card 2
    st.markdown(f"""
        <div class="teacher-card">
            <img src="data:image/jpeg;base64,{t2}" class="teacher-img">
            <div class="teacher-content">
                <div class="teacher-name">ครูพี่คอส</div>
                <div class="teacher-detail"><b>การศึกษา:</b> ปริญญาตรี เกียรตินิยม จุฬาลงกรณ์มหาวิทยาลัย สาขาคณิตศาสตร์ประกันภัย</div>
                <div class="teacher-detail"><b>ประสบการณ์:</b> 4 ปี</div>
                <div class="teacher-detail"><b>ความเชี่ยวชาญ:</b> โอลิมปิกคณิตศาสตร์, TPAT1, ONET</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Card 3
    st.markdown(f"""
        <div class="teacher-card">
            <img src="data:image/jpeg;base64,{t3}" class="teacher-img">
            <div class="teacher-content">
                <div class="teacher-name">ครูพี่คิม</div>
                <div class="teacher-detail"><b>การศึกษา:</b> ปริญญาตรี เกียรตินิยม ครุศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย</div>
                <div class="teacher-detail"><b>ประสบการณ์:</b> 2 ปี</div>
                <div class="teacher-detail"><b>ความเชี่ยวชาญ:</b> ปูพื้นฐานแน่น เข้าใจง่าย</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)