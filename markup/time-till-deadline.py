import datetime
user_input = input("enter your goal  withe a deadline separated by a colon\n")
input_list =user_input.split(":")

goal  = input_list[0]
deadline = input_list[1]

deadline_date =datetime.datetime.strptime(deadline,"%d.%m.%Y")
# print(type(datetime.datetime.strptime(deadline,"%d.%m.%Y")))
today_date = datetime.datetime.today()
# calculate  how many  days  form  now till ddealine
time_till = deadline_date - today_date

hours_till = int(time_till.total_seconds() / 60 / 60)
print(f"Dear user Time remaining for your  goal: {goal} is {hours_till}")


#print(input_list)

""" 
enter your goal  withe a deadline separated by a colon
learn py:12.12.2025
2025-12-12 00:00:00
<class 'datetime.datetime'>

Process finished with exit code 0
"""