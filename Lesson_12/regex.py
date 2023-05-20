import re


pattern = 'This'
my_string = 'This is my text. text is good (099)333-33-33'
date_string = '12/12/2022'
phone_string = '(099)-333-33-33'

date_format = r'^[\d.-]+$'
phone_format = r'[\d+\-()]+$'


result = re.match(date_format, date_string)
print(result)


result = re.match(phone_format, phone_string)
print(result)

search_result = re.search(phone_format, my_string)
print(search_result)


find_all_result = re.findall('text', my_string)
print(find_all_result)


result_split = re.split('is', my_string, maxsplit=2)
print(result_split)


result_sub = re.sub('text','python', my_string)
print(result_sub)


match_result = re.match(r'[a-z0-9A-Z_-]{6-16}$', 'aScsd_d-4d')
print(match_result)


