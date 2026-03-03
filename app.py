import json
from PIL import Image
import streamlit as st

logo = Image.open("logo.png")

st.set_page_config(
    page_title="ZeeU TUTOR",
    page_icon=logo,  
    layout="wide"
)

st.set_page_config(page_title="ZeeU TUTOR", layout="wide")

# ------------------ LOAD QUESTIONS ------------------


def load_questions(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

st.markdown("""
<style>

/* ===== ANNOUNCEMENT BAR ===== */
.announce {
    background: #1e40af;
    color: white;
    text-align: center;
    padding: 8px;
    font-size: 14px;
}

/* ===== NAVBAR ===== */
.navbar {
    background: white;
    padding: 18px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.nav-logo {
    font-size: 24px;
    font-weight: 800;
    color: #1e3a8a;
}

/* ===== HERO ===== */
.hero {
    background-image: url("https://images.pexels.com/photos/5212345/pexels-photo-5212345.jpeg?auto=compress&cs=tinysrgb&w=1600");
    background-size: cover;
    background-position: center;
    position: relative;
    padding: 160px 20px;
    text-align: center;
    color: white;
    border-radius: 0 0 40px 40px;
}

.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.55);
    border-radius: 0 0 40px 40px;
}

.hero-content {
    position: relative;
    z-index: 2;
}

.hero h1 {
    font-size: 72px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    font-size: 24px;
    margin-top: 20px;
}

/* ===== BUTTON ===== */
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

/* ===== CONTACT CARD ===== */
.contact-box {
    margin-top: 60px;
    padding: 30px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    font-size: 18px;
    text-align: center;
}

/* ===== EXAM CARD ===== */
.exam-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ------------------ SESSION ------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ================== HOME ==================
if st.session_state.page == "home":

    # Announcement Bar
    st.markdown("""
    <div class="announce">
        🎉 เปิดรับสมัครรอบใหม่แล้ว! รับจำนวนจำกัด
    </div>
    """, unsafe_allow_html=True)

    # Navbar
    nav1, nav2, nav3, nav4 = st.columns([3,1,1,1])

    with nav1:
        st.markdown("### ZeeU TUTOR")

    with nav2:
        if st.button("ทดลองทำข้อสอบ"):
            st.session_state.page = "select_exam"
            st.rerun()

    with nav3:
        if st.button("สมัครเรียน"):
            st.session_state.page = "register"
            st.rerun()

    with nav4:
        if st.button("ติดต่อ"):
            st.session_state.page = "home"
            st.rerun()

    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <h1>ZeeU TUTOR</h1>
            <p>เตรียมสอบเข้า ม.1 & ม.4 แบบมืออาชีพ<br>
            สร้างความเข้าใจระยะยาว คิดวิเคราะห์เป็นระบบ</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    st.markdown("""
    <div class="contact-box">
        <b>ติดต่อเรา</b><br><br>
        📘 Facebook: ZeeuTUTOR <br>
        💬 Line: openchat ZeeuTUTOR <br>
        📞 Phone: 065-294-1928
    </div>
    """, unsafe_allow_html=True)
# ================== SELECT EXAM ==================
elif st.session_state.page == "select_exam":

    st.title("เลือกระดับข้อสอบ")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎯 ทำข้อสอบ ม.1"):
            st.session_state.level = "m1"
            st.session_state.page = "exam"

    with col2:
        if st.button("🚀 ทำข้อสอบ ม.4"):
            st.session_state.level = "m4"
            st.session_state.page = "exam"

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

        # แสดงรูปถ้ามี
        if q["image"]:
            st.image(q["image"], width=300)

        # ถ้ามีตัวเลือก → ใช้ radio
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
        st.success(f"ขอบคุณคุณ {name} ทางเราจะติดต่อกลับเร็วที่สุด")

    if st.button("⬅ กลับหน้าแรก"):
        st.session_state.page = "home"
