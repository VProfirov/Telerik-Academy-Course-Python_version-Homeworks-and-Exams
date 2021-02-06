from datetime import datetime

def get_current_datetime():
    current_datetime = datetime.now().strftime('%d %b %Y')
    return current_datetime


if __name__ == '__main__':
    print(f'The current date is: {get_current_datetime()}')
