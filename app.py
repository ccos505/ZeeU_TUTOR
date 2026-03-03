from PIL import Image
import streamlit as st

logo = Image.open("logo.png")

st.set_page_config(
    page_title="ZeeU TUTOR",
    page_icon=logo,
    layout="wide"
)

# ------------------ MODERN LIGHT CSS ------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #f8fafc, #e2e8f0);
    padding: 120px 20px;
    text-align: center;
    border-radius: 20px;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 64px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 10px;
}

.hero p {
    font-size: 22px;
    color: #374151;
}

/* Buttons */
.stButton>button {
    border-radius: 14px;
    height: 52px;
    font-weight: 600;
    background: linear-gradient(135deg, #2563eb, #1e40af);
    color: white;
    border: none;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* Cards */
.exam-box {
    background: #ffffff;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.05);
    margin-bottom: 25px;
}

/* Contact */
.contact-box {
    margin-top: 40px;
    padding: 25px;
    background: #ffffff;
    border-radius: 16px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    font-size: 18px;
    text-align: center;
}

/* Titles */
h1, h2, h3 {
    color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ------------------ SESSION ------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ================== HOME ==================
if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <h1>ZeeU TUTOR</h1>
        <p>เตรียมสอบเข้า M1 & M4 แบบมืออาชีพ<br>
        สอนเข้าใจลึก คิดวิเคราะห์เป็นระบบ</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 เริ่มทำข้อสอบ"):
            st.session_state.page = "select_exam"

    with col2:
        if st.button("📝 สมัครเรียน"):
            st.session_state.page = "register"

    st.markdown("""
    <div class="contact-box">
        <b>ติดต่อเรา</b><br><br>
        📘 Facebook: ZeeuTUTOR<br>
        💬 Line: openchat ZeeuTUTOR<br>
        📞 Phone: 065-294-1928
    </div>
    """, unsafe_allow_html=True)
