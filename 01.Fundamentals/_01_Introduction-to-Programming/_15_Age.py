from datetime import datetime

def get_current_age(birthdate_str):
    current_date = datetime.now()
    birth_date = datetime.strptime(birthdate_str,'%d.%m.%Y')
    current_age = current_date.year - birth_date.year

    if (birth_date.date() > current_date.replace(year= current_date.year - current_age).date()):
        current_age -= 1
    return current_age


def get_age_after_10years(age):
    return age + 10


if __name__ == '__main__':
    # get_current_age('10.05.1990')
    birthdate = '10.05.1987'
    current_age = get_current_age(birthdate)
    age_after_10years = get_age_after_10years(current_age)
    print(current_age)
    print(age_after_10years)
