from datetime import datetime
time_input = input()
time_obj = datetime.strptime(time_input, '%H:%M')
print(time_obj.strftime('%I:%M %p'))