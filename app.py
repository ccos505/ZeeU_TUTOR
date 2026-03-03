from PIL import Image
import streamlit as st

logo = Image.open("logo.png")

st.set_page_config(
    page_title="ZeeU TUTOR",
    page_icon=logo,  
    layout="wide"
)

# -----------------------
# CUSTOM CSS (Modern)
# -----------------------
st.markdown("""
<style>
.header {
    background: linear-gradient(135deg, #000000, #2c2c2c);
    padding: 100px 0;
    text-align: center;
    color: white;
}

.header h1 {
    font-size: 64px;
    font-weight: 800;
    margin: 0;
}

.header p {
    font-size: 20px;
    opacity: 0.8;
}

.card-container {
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-top: 60px;
}

.card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    width: 300px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.12);
}

.exam-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.stButton>button {
    border-radius: 12px;
    height: 50px;
    font-weight: 600;
    background-color: black;
    color: white;
}

.stButton>button:hover {
    background-color: #333;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# LOAD QUESTIONS
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
# SESSION STATE
# -----------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# -----------------------
# HOME PAGE
# -----------------------
if st.session_state.page == "home":

    st.markdown("""
    <div class="header">
        <h1>ZeeU TUTOR</h1>
        <p>เตรียมสอบเข้า M1 & M4 แบบมืออาชีพ</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🎯 สอบเข้า M1")
        st.write("แบบฝึกหัดพื้นฐานสำหรับนักเรียน ม.1")
        if st.button("เริ่มทำข้อสอบ M1"):
            st.session_state.level = "m1"
            st.session_state.page = "exam"
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🚀 สอบเข้า M4")
        st.write("แบบฝึกหัดสอบเข้า ม.4 ระดับกลาง-สูง")
        if st.button("เริ่มทำข้อสอบ M4"):
            st.session_state.level = "m4"
            st.session_state.page = "exam"
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------
# EXAM PAGE
# -----------------------
elif st.session_state.page == "exam":

    st.markdown("## 📝 แบบทดสอบ")

    questions = load_questions(f"{st.session_state.level}.txt")

    score = 0
    total = len(questions)
    user_answers = []

    progress = st.progress(0)

    for idx, q in enumerate(questions):
        st.markdown('<div class="exam-box">', unsafe_allow_html=True)
        st.write(f"### ข้อ {q['no']}")
        st.write(q["question"])
        ans = st.text_input("คำตอบของคุณ", key=q["no"])
        user_answers.append((q, ans))
        st.markdown('</div>', unsafe_allow_html=True)

        progress.progress((idx + 1) / total)

    if st.button("ส่งคำตอบ"):
        for q, ans in user_answers:
            if ans.strip() == q["answer"]:
                score += 1

        st.success(f"🎉 คะแนนของคุณ: {score} / {total}")

        if score == total:
            st.balloons()

    if st.button("⬅ กลับหน้าแรก"):
        st.session_state.page = "home"
