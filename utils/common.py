
from datetime import datetime
def generate_password():
    today = datetime.today()
    yy = today.year % 100
    mm = today.month
    dd = today.day
    
    total = yy + mm + dd
    return str(total).zfill(4)[::-1] 