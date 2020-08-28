import datetime
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
b_year, b_month, b_day = map(int,input('생년월일을 입력해주세요.> ').split())
if current_month > b_month:                   # 현재월 > 생월
    age = current_year - b_year
elif current_month < b_month:                 # 현재월 < 생월
    age = current_year - b_year - 1
else:                                         # 현재월 == 생월
    if current_day < b_day:                      # 현재일 < 생일
        age = current_year - b_year - 1          
    else:                                        # 현재일 >= 생일
        age = current_year - b_year


print('만 나이는 %d 입니다.' % age)