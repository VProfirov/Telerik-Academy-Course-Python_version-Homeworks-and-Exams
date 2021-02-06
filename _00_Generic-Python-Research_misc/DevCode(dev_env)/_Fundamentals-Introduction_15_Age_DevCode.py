from datetime import datetime
# import datetime

def get_current_age(birthdate_str):
    current_date = datetime.now()
    birth_date = datetime.strptime(birthdate_str,'%d.%m.%Y')
    current_age = current_date.year - birth_date.year
    print( "----------  " + str(birth_date.date()))
    if (birth_date.date() > current_date.replace(year= current_date.year - current_age).date()):
        # print(birth_date.date())
        # print(current_date.replace(year= current_date.year - current_age).date())
        # print(current_age)
        current_age -= 1
        # print(current_age)
        # print('----------end of if ------------------')
    return current_age

    # current_age_in_days = current_date - birth_date
    return current_age


# def get_age_after_10years():


# get_current_age('10.05.1990')
birthdate = '10.05.1987'
print(get_current_age(birthdate))


def utility_tmp_function():
    current_date = datetime.now()
    print(datetime.strptime('10.10.1990','%d.%m.%Y'))
    print(current_date)
    print(type(current_date))
    print('----')
    print(current_date.strftime('%d.%m.%Y'))
    print('------------')
    print(type(current_date.strftime('%d.%m.%Y')))
    print(type(datetime.strptime(current_date.strftime('%d.%m.%Y'),'%d.%m.%Y')))
    # print(str(type(datetime(current_date.strftime('%d.%m.%Y')))))
    print('-------------------')
