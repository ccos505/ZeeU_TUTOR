import streamlit as st

# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(
    page_title="ZeeU TUTOR",
    layout="wide",
    page_icon="📚"
)

# --------------------------------
# Custom CSS (Modern UI)
# --------------------------------
st.markdown("""
<style>
html, body {
    margin: 0;
    padding: 0;
}

.header {
    background-image: url('https://images.pexels.com/photos/4145195/pexels-photo-4145195.jpeg?auto=compress&cs=tinysrgb&w=1200');
    background-size: cover;
    background-position: center;
    padding: 120px 0;
    text-align: center;
    color: #FFFFFF;
    backdrop-filter: brightness(0.6);
}

.header h1 {
    font-size: 72px;
    font-weight: bold;
    margin: 0;
}

.header p {
    font-size: 22px;
    margin-top: 10px;
    opacity: 0.9;
}

.btn-modern {
    background-color: #000;
    color: #fff;
    padding: 15px 30px;
    font-weight: 600;
    border-radius: 10px;
    text-decoration: none;
    transition: 0.3s;
    display: inline-block;
}

.btn-modern:hover {
    background-color: #333;
    color: #fff;
    transform: translateY(-3px);
}

.level-cards {
    padding: 60px 0;
    display: flex;
    justify-content: space-around;
}

.card {
    width: 280px;
    background: #fff;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    box-shadow: 0px 15px 30px rgba(0,0,0,0.12);
    transform: translateY(-5px);
}

.card h3 {
    font-size: 28px;
    margin-bottom: 10px;
}

.card p {
    color: #555;
    font-size: 16px;
}

.footer {
    text-align: center;
    margin-top: 80px;
    padding: 40px 0;
    color: #888;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------
# Hero Section
# --------------------------------
st.markdown("""
<div class="header">
    <h1>ZeeU TUTOR</h1>
    <p>เตรียมสอบเข้า M1 & M4 ด้วยแบบฝึกหัดคุณภาพ</p>
    <a class="btn-modern" href="#levels">เริ่มเลย</a>
</div>
""", unsafe_allow_html=True)

# --------------------------------
# Cards Section
# --------------------------------
st.markdown('<div id="levels" class="level-cards">', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>📘 สอบเข้า M1</h3>
    <p>แบบฝึกหัดคัดกรองพื้นฐาน เพิ่มความมั่นใจ</p>
    <a class="btn-modern" href="#m1">ทำข้อสอบ M1</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>📗 สอบเข้า M4</h3>
    <p>โจทย์ระดับกลาง-สูง พร้อมเฉลย</p>
    <a class="btn-modern" href="#m4">ทำข้อสอบ M4</a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------
# Footer
# --------------------------------
st.markdown("""
<div class="footer">
    © 2026 ZeeU TUTOR — เว็บฝึกสอบออนไลน์
</div>
""", unsafe_allow_html=True)
