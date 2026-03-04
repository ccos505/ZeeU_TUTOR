
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit as st
import json
import os
from datetime import datetime, timedelta

SUBMIT_LOG_FILE = "submit_log.json"
import re

def generate_password():
    today = datetime.today()
    yy = today.year % 100
    mm = today.month
    dd = today.day
    
    total = yy + mm + dd
    return str(total).zfill(4)[::-1] 


def send_exam_result_email(student_name, level, test_type, score, total, result_detail):

    sender_email = st.secrets["EMAIL_USER"]
    sender_password = st.secrets["EMAIL_PASS"]
    receiver_email = st.secrets["EMAIL_USER"]
    date = datetime.now().strftime("%Y-%m-%d")

    subject = f"ผลสอบ {student_name} ระดับ {level.upper()} ({test_type}) - วันที่ {date}"

    body = f"""
        📚 ผลสอบ

        ชื่อ: {student_name}
        ระดับ: {level.upper()}
        ประเภท: {test_type}
        คะแนน: {score} / {total}

        -------------------------
        รายละเอียดแต่ละข้อ
        -------------------------
        """

    for item in result_detail:
        body += f"""
            ข้อ {item['no']}
            ตอบ: {item['user_answer']}
            เฉลย: {item['correct_answer']}
            ผลลัพธ์: {item['result']}
            -------------------------
            """

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการส่งอีเมล: {e}")
        return False



def send_email(name, grade, phone):
    try:
        # --------- Load Secrets ----------
        sender_email = st.secrets["EMAIL_USER"]
        sender_password = st.secrets["EMAIL_PASS"]
        receiver_emails = st.secrets["EMAIL_RECEIVER"]

        if isinstance(receiver_emails, str):
            receiver_emails = [receiver_emails]

        # --------- Email Content ----------
        subject = "มีผู้สมัครเรียนใหม่ - ZeeU TUTOR"
        body = f"""
        ========================================
                📌 แจ้งเตือนผู้สมัครเรียนใหม่
        ========================================

        👤 ชื่อ-นามสกุล : {name}
        🎓 ระดับชั้น     : {grade}
        📞 เบอร์โทรศัพท์ : {phone}

        ----------------------------------------
        กรุณาติดต่อกลับโดยเร็วที่สุด
        ========================================
        """

        msg = MIMEText(body, "plain", "utf-8")
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = ", ".join(receiver_emails)

        # --------- Send Email ----------
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(sender_email, sender_password)
            server.sendmail(
                sender_email,
                receiver_emails,
                msg.as_string()
            )

        return True 

    except KeyError as e:
        st.error(f"❌ Missing secret key: {e}")
        return False

    except smtplib.SMTPAuthenticationError:
        st.error("❌ Email login failed. ตรวจสอบ App Password")
        return False

    except smtplib.SMTPException as e:
        st.error(f"❌ SMTP Error: {e}")
        return False

    except Exception as e:
        st.error(f"❌ Unexpected Error: {e}")
        return False
    
    
def is_valid_phone(phone):
    digits_only = "".join(c for c in phone if c.isdigit())
    if len(digits_only) in [9, 10]:
        return True
    return False


def clean_student_name(name: str) -> str:
    if not name:
        return ""
    name = name.strip()
    name = re.sub(r"\s+", " ", name)
    name = re.sub(r"[^a-zA-Zก-๙\s]", "", name)
    name = name.lower()

    return name


def can_submit(student_name, level, test_type):

    key = f"{student_name}_{level}_{test_type}"
    
    if not os.path.exists(SUBMIT_LOG_FILE):
        return True

    with open(SUBMIT_LOG_FILE, "r") as f:
        data = json.load(f)

    if key not in data:
        return True

    last_submit_time = datetime.fromisoformat(data[key])
    if datetime.now() - last_submit_time < timedelta(hours=1):
        return False

    return True

def save_submit_time(student_name, level, test_type):

    key = f"{student_name}_{level}_{test_type}"

    if os.path.exists(SUBMIT_LOG_FILE):
        with open(SUBMIT_LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[key] = datetime.now().isoformat()

    with open(SUBMIT_LOG_FILE, "w") as f:
        json.dump(data, f)