import streamlit as st
import base64

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="ZeeU TUTOR",
    page_icon="📚",
    layout="wide"
)

# -----------------------
# Custom CSS (Minimal Modern)
# -----------------------
st.markdown("""
<style>

body {
    background-color: #f8f9fa;
}

.main {
    padding: 2rem;
}

.big-title {
    font-size: 48px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: gray;
    margin-bottom: 40px;
}

.level-card {
    padding: 40px;
    border-radius: 20px;
    background: white;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    text-align: center;
    transition: 0.3s;
}

.level-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.12);
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-weight: 600;
    background-color: black;
    color: white;
}

.stButton>button:hover {
    background-color: #333333;
    color: white;
}

.exam-box {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# Load Logo
# -----------------------
st.image("logo.png", width=120)

st.markdown('<div class="big-title">ZeeU TUTOR</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Math Practice Exam Platform</div>', unsafe_allow_html=True)

# -----------------------
# Load Questions
# -----------------------
def load_questions(file_name):
    questions = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                questions.append({
                    "no": parts[0],
                    "question": parts[1],
                    "answer": parts[2]
                })
    return questions

# -----------------------
# Session State
# -----------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------
# HOME PAGE
# -----------------------
if st.session_state.page == "home":

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="level-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 สอบเข้า M1")
        st.write("แบบฝึกหัดพื้นฐาน ม.1")
        if st.button("เริ่มทำข้อสอบ M1"):
            st.session_state.level = "m1"
            st.session_state.page = "exam"
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="level-card">', unsafe_allow_html=True)
        st.markdown("### 🚀 สอบเข้า M4")
        st.write("แบบฝึกหัดสอบเข้า ม.4")
        if st.button("เริ่มทำข้อสอบ M4"):
            st.session_state.level = "m4"
            st.session_state.page = "exam"
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# EXAM PAGE
# -----------------------
elif st.session_state.page == "exam":

    st.markdown("---")
    st.markdown(f"## 📝 ข้อสอบระดับ {st.session_state.level.upper()}")

    questions = load_questions(f"{st.session_state.level}.txt")
    score = 0
    user_answers = []

    for q in questions:
        st.markdown('<div class="exam-box">', unsafe_allow_html=True)
        st.write(f"### ข้อ {q['no']}")
        st.write(q["question"])
        ans = st.text_input("คำตอบของคุณ", key=q["no"])
        user_answers.append((q, ans))
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("ส่งคำตอบ"):
        for q, ans in user_answers:
            if ans.strip() == q["answer"]:
                score += 1

        st.success(f"🎉 คะแนนของคุณ: {score} / {len(questions)}")

        if score == len(questions):
            st.balloons()

    if st.button("⬅ กลับหน้าแรก"):
        st.session_state.page = "home"
