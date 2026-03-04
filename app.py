import os
from PIL import Image
import streamlit as st
from utils.image_utils import get_base64
from utils.question_loader import load_questions
from utils.common import generate_password, send_email
from styles.main_style import apply_style
from pages.home import render_home

logo = Image.open("logo.png")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
st.set_page_config(
    page_title="ZeeU TUTOR",
    page_icon=logo,  
    layout="wide"
)

st.set_page_config(page_title="ZeeU TUTOR", layout="wide")
# Load images
bg1 = get_base64("assets/hero1.jpg")
bg2 = get_base64("assets/hero2.jpg")
bg3 = get_base64("assets/hero3.jpg")
bg4 = get_base64("assets/hero4.jpg")
fb_icon = get_base64("assets/facebook.png")
line_icon = get_base64("assets/line.png")
phone_icon = get_base64("assets/phone.png")

# Apply style
st.markdown(apply_style(bg1,bg2,bg3,bg4), unsafe_allow_html=True)

# Page routing
if "page" not in st.session_state:
    st.session_state.page = "home"
    
    
if "ask_password" not in st.session_state:
    st.session_state.ask_password = False

if st.session_state.page == "home":
    

    # Announcement Bar
    st.markdown("""
    <div class="announce">
        🎉 เปิดรับสมัครรอบใหม่แล้ว! รับจำนวนจำกัด
    </div>
    """, unsafe_allow_html=True)

    # Navbar
    nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns([3,1,1,1,1,1,1])

    with nav1:
        st.markdown("### ZeeU TUTOR")

    with nav2:
        if st.button("ทดลองทำข้อสอบ"):
            st.session_state.ask_password = True
            # st.session_state.page = "select_exam"
            # st.rerun()

    with nav3:
        if st.button("สมัครเรียน"):
            st.session_state.page = "register"
            st.rerun()

    with nav4:
        if st.button("ติดต่อ"):
            # st.session_state.page = "contact"
            st.session_state.page = "home"
            st.rerun()

    with nav5:
        if st.button("คอร์สเรียน"):
            # st.session_state.page = "courses"
            st.session_state.page = "home"
            st.rerun()

    with nav6:
        if st.button("โปรโมชัน"):
            # st.session_state.page = "promotion"
            st.session_state.page = "home"
            st.rerun()

    with nav7:
        if st.button("ทดลองเรียนฟรี"):
            # st.session_state.page = "free_trial"
            st.session_state.page = "home"
            st.rerun()
                
    if st.session_state.ask_password:
        st.markdown('<div class="dimmed">', unsafe_allow_html=True)
        
        
    if st.session_state.ask_password:
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="password-wrapper">', unsafe_allow_html=True)

        st.markdown(
            '<div class="password-title">🔐 กรุณากรอกรหัสก่อนเข้าใช้งาน</div>',
            unsafe_allow_html=True
        )

        user_input = st.text_input(
            "รหัสยืนยัน",
            type="password",
            label_visibility="collapsed"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("ยืนยัน", use_container_width=True):
                if user_input == generate_password():
                    st.session_state.ask_password = False
                    st.session_state.page = "select_exam"
                    st.rerun()
                else:
                    st.error("❌ รหัสไม่ถูกต้อง")

        with col2:
            if st.button("ยกเลิก", use_container_width=True):
                st.session_state.ask_password = False
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
            
    render_home()

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)
    st.markdown(f"""
    <div class="footer">
    <div class="footer-content">
    <div class="footer-title">
    ZeeU TUTOR | ติดต่อเรา
    </div>

    <div class="footer-links">

    <a href="https://www.facebook.com/profile.php?id=61586686648790"
    target="_blank"
    class="footer-item">
        <img src="data:image/png;base64,{fb_icon}">
        <span>ZeeuTUTOR</span>
    </a>

    <a href="https://line.me/ti/g2/Xz8aX7jDsDKEsJKESX6-cCcWg8vNKrRNnLiy-g"
    target="_blank"
    class="footer-item">
        <img src="data:image/png;base64,{line_icon}">
        <span>OpenChat</span>
    </a>

    <a href="tel:0652941928"
    class="footer-item">
        <img src="data:image/png;base64,{phone_icon}">
        <span>065-294-1928</span>
    </a>

    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# ================== SELECT EXAM ==================
elif st.session_state.page == "select_exam":

    st.title("เลือกระดับข้อสอบ")

    # ===== สร้าง 3 คอลัมน์ =====
    col1, col2, col3 = st.columns(3)

    # ===== ROW 1 =====
    with col1:
        if st.button("🎯 ทำข้อสอบ ม.1"):
            st.session_state.level = "m1"
            st.session_state.page = "exam"

    with col2:
        if st.button("📘 ทำข้อสอบ ม.2"):
            st.warning("🚧 ระดับ ม.2 กำลังพัฒนา")

    with col3:
        if st.button("📗 ทำข้อสอบ ม.3"):
            st.warning("🚧 ระดับ ม.3 กำลังพัฒนา")
    # ===== ROW 2 =====
    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("🚀 ทำข้อสอบ ม.4"):
            st.session_state.level = "m4"
            st.session_state.page = "exam"

    with col5:
        if st.button("📙 ทำข้อสอบ ม.5"):
            st.warning("🚧 ระดับ ม.5 กำลังพัฒนา")

    with col6:
        if st.button("🎓 ทำข้อสอบ ม.6"):
            st.warning("🚧 ระดับ ม.6 กำลังพัฒนา")

    # ===== ปุ่มกลับ =====
    if st.button("⬅ กลับหน้าแรก"):
        st.session_state.page = "home"

# ================== EXAM PAGE ==================
elif st.session_state.page == "exam":

    st.title(f"ข้อสอบระดับ {st.session_state.level.upper()}")

    questions = load_questions(f"questions/{st.session_state.level}.json")
    score = 0
    user_answers = []

    for q in questions:
        st.markdown('<div class="exam-box">', unsafe_allow_html=True)
        st.subheader(f"ข้อที่ {q['no']}")
        st.write(q["question"])

        if q.get("image"):
            image_path = os.path.join(BASE_DIR, q["image"])
            if os.path.exists(image_path):
                st.image(image_path, width=300)
                
        if q["choices"]:
            ans = st.radio(
                "เลือกคำตอบ",
                q["choices"],
                key=f"q_{q['no']}"
            )
        else:
            ans = st.text_input(
                "คำตอบ",
                key=f"q_{q['no']}"
            )
        user_answers.append((q, str(ans)))
        st.markdown('</div>', unsafe_allow_html=True)
    score = 0

    if st.button("ส่งคำตอบ"):
        for q, ans in user_answers:
            if str(ans.strip()) == str(q["answer"]):
                score += 1

        st.success(f"คุณได้ {score} / {len(questions)} คะแนน")

    if st.button("⬅ กลับหน้าเลือกข้อสอบ"):
        st.session_state.page = "select_exam"

# ================== REGISTER ==================
elif st.session_state.page == "register":

    st.title("สมัครเรียน")

    name = st.text_input("ชื่อ-นามสกุล")
    grade = st.text_input("ระดับชั้น")
    phone = st.text_input("เบอร์โทรศัพท์")

    if st.button("ยืนยันสมัคร"):
        send_email(name, grade, phone)
        st.success(f"ขอบคุณคุณ {name} ทางเราจะติดต่อกลับเร็วที่สุด")

    if st.button("⬅ กลับหน้าแรก"):
        st.session_state.page = "home"
