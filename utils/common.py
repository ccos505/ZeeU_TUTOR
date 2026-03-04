
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
            มีผู้สมัครเรียนใหม่

            ชื่อ: {name}
            ระดับชั้น: {grade}
            เบอร์โทร: {phone}
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

        return True  # success

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
    # ดึงเฉพาะตัวเลข 0-9 ออกมา
    digits_only = "".join(c for c in phone if c.isdigit())

    # ตรวจสอบว่ามี 9 หรือ 10 หลัก
    if len(digits_only) in [9, 10]:
        return True
    return False