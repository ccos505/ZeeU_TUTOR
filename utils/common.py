
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import streamlit as st


def generate_password():
    today = datetime.today()
    yy = today.year % 100
    mm = today.month
    dd = today.day
    
    total = yy + mm + dd
    return str(total).zfill(4)[::-1] 




def send_email(name, grade, phone):
    sender_email = st.secrets["EMAIL_USER"]
    sender_password = st.secrets["EMAIL_PASS"]
    receiver_email = st.secrets["EMAIL_RECEIVER"]

    subject = "มีผู้สมัครเรียนใหม่ - ZeeU TUTOR"
    body = f"""
    มีผู้สมัครใหม่

    ชื่อ: {name}
    ระดับชั้น: {grade}
    เบอร์โทร: {phone}
    """

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())