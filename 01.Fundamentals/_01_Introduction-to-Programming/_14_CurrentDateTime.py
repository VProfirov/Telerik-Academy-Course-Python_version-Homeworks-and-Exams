from datetime import datetime

def get_current_datetime():
    current_datetime = datetime.now().strftime('%d %b %Y')
    return current_datetime


print(get_current_datetime())
