import time


# time.sleep(4)

localtime = time.localtime()
print(localtime)

# time.struct_time

print(localtime.tm_year)


my_date_tuple = (2022, 12, 12, 20, 30, 15, 11, 340, 1)

mktime = time.mktime(localtime)
print(mktime)

mktime_tuple = time.mktime(my_date_tuple)
print(mktime_tuple)

print(time.asctime(my_date_tuple))

localtime = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", my_date_tuple)
print(time_string)

my_date = "2022, 20:22:40 15 June"
result = time.strptime(my_date, "%Y, %H:%M:%S %d %B")
print(result)
print(type(result))

print(time.asctime(result))
