import streamlit as st
from pathlib import Path
import os
from utils.image_utils import get_base64


BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"

def render_home():
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <h1>ZeeU TUTOR</h1>
            <p>เตรียมสอบเข้า ม.1 - ม.6 แบบมืออาชีพ</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
def render_teachers():

    # ===== CSS STYLE =====
    st.markdown("""
    <style>
    .teacher-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        height: 100%;
    }

    .teacher-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.1);
    }

    .teacher-img {
        width: 100%;
        border-radius: 12px;
        margin-bottom: 15px;
        transition: transform 0.3s ease;
    }

    .teacher-card:hover .teacher-img {
        transform: scale(1.05);
    }

    .teacher-name {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 10px;
        color: #1e3a8a;
    }

    .teacher-info {
        font-size: 14px;
        color: #444;
        line-height: 1.6;
    }

    @media (max-width: 768px) {
        .teacher-card {
            margin-bottom: 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 👩‍🏫 คุณครูของเรา")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    # ===== Teacher 1 =====
    with col1:
        t1 = get_base64(ASSETS_DIR / "teacher1.jpg")

        st.markdown(f"""
        <div class="teacher-card">
            <img src="data:image/jpeg;base64,{t1}" class="teacher-img">
            <div class="teacher-name">ครูนก</div>
            <div class="teacher-info">
                <b>การศึกษา:</b> ปริญญาตรี คณิตศาสตร์ <br>
                <b>ประสบการณ์:</b> 20 ปี <br>
                <b>ความเชี่ยวชาญ:</b> คณิตศาสตร์
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ===== Teacher 2 =====
    with col2:
        t2 = get_base64(ASSETS_DIR / "teacher2.jpg")

        st.markdown(f"""
        <div class="teacher-card">
            <img src="data:image/jpeg;base64,{t2}" class="teacher-img">
            <div class="teacher-name">ครูพี่คอส</div>
            <div class="teacher-info">
                <b>การศึกษา:</b> ปริญญาตรี เกียรตินิยม จุฬาฯ คณิตศาสตร์ประกันภัย <br>
                <b>ประสบการณ์:</b> 4 ปี <br>
                <b>ความเชี่ยวชาญ:</b> โอลิมปิกคณิต, TPAT1, ONET
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ===== Teacher 3 =====
    with col3:
        t3 = get_base64(ASSETS_DIR / "teacher3.jpg")

        st.markdown(f"""
        <div class="teacher-card">
            <img src="data:image/jpeg;base64,{t3}" class="teacher-img">
            <div class="teacher-name">ครูพี่คิม</div>
            <div class="teacher-info">
                <b>การศึกษา:</b> ปริญญาตรี เกียรตินิยม ครุศาสตร์ จุฬาฯ <br>
                <b>ประสบการณ์:</b> 2 ปี <br>
                <b>ความเชี่ยวชาญ:</b> ปูพื้นฐานแน่น เข้าใจง่าย
            </div>
        </div>
        """, unsafe_allow_html=True)
