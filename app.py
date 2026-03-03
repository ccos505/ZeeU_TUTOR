import streamlit as st

st.set_page_config(page_title="ZeeU TUTOR - Practice Exam")

st.title("📚 ZeeU TUTOR")
st.subheader("แบบฝึกหัดเตรียมสอบเข้า")

# -----------------------
# Function อ่านไฟล์
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
# หน้าเลือกข้อสอบ
# -----------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.markdown("### เลือกระดับข้อสอบ")
    
    if st.button("📝 ทดลองสอบเข้า M1"):
        st.session_state.level = "m1"
        st.session_state.page = "exam"

    if st.button("📝 ทดลองสอบเข้า M4"):
        st.session_state.level = "m4"
        st.session_state.page = "exam"


# -----------------------
# หน้าแสดงข้อสอบ
# -----------------------
elif st.session_state.page == "exam":

    file_name = f"{st.session_state.level}.txt"
    questions = load_questions(file_name)

    st.write(f"## ข้อสอบระดับ {st.session_state.level.upper()}")

    score = 0

    user_answers = []

    for q in questions:
        st.write(f"### ข้อ {q['no']}: {q['question']}")
        ans = st.text_input("คำตอบ", key=q["no"])
        user_answers.append((q, ans))

    if st.button("ส่งคำตอบ"):
        for q, ans in user_answers:
            if ans.strip() == q["answer"]:
                score += 1

        st.success(f"คะแนนของคุณคือ {score} / {len(questions)}")

        if score == len(questions):
            st.balloons()

    if st.button("⬅ กลับหน้าแรก"):
        st.session_state.page = "home"
