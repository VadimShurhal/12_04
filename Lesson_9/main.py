import datetime


now = datetime.datetime.now()
print(now)

currunt_date = datetime.date.today()
print(currunt_date)


current_datetime = datetime.datetime.now()
current_time = current_datetime.time()

print(current_time)
print(type(current_time))


time_obj = datetime.time(12, 35, 20)
print(time_obj)

date_obj = datetime.datetime(2022, 11, 20, 15, 20, 20)
print(date_obj)


date_1 = datetime.datetime(2022, 10, 20, 15, 20, 20)
date_2 = datetime.datetime(2022, 11, 20, 15, 10, 20)


delta = date_2 - date_1
print(delta)


if date_2 > date_1:
    print("Hello !")

# # today = datetime.date.today()
# print(f'Our date {date_2}')
# new_date = date_2 + datetime.timedelta(seconds=7)
# print(f'After 7 minutes {new_date}')


today = datetime.date.today()
print(f'Our date {today}')
new_date = today + datetime.timedelta(days=7)
print(f'After 7 days {new_date}')


print(datetime.datetime.timestamp(date_2))

