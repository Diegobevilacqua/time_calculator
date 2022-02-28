def to_24_hours_format(time):
    time_without_period = time.split(' ')[0]
    period = time.split(' ')[1]
    if (period == 'AM'):
        return time.split(' ')[0]
    hours = str(int(time_without_period.split(':')[0]) + 12)
    minutes = time_without_period.split(':')[1]
    return hours + ':' + minutes

def to_12_hours_format(time):
    time_without_period = time.split(' ')[0]
    hours = str(int(time_without_period.split(':')[0]) % 24)
    minutes = time_without_period.split(':')[1]
    if (int(hours) >= 12):
        if (int(hours) == 12):
            return '12:' + minutes.zfill(2) + ' PM'
        return str(int(hours) - 12) + ':' + minutes.zfill(2) + ' PM'
    else:
        if (int(hours) == 0):
            return '12:' + minutes.zfill(2) + ' AM'
        return hours + ':' + minutes.zfill(2) + ' AM'

def add_time_to_start(start, duration):
    _24_hours_format_start = to_24_hours_format(start)
    time_hours = int(_24_hours_format_start.split(':')[0])
    time_minutes = int(_24_hours_format_start.split(':')[1])
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
    hours = (time_hours + duration_hours + (time_minutes + duration_minutes) // 60) % 24
    minutes = (time_minutes + duration_minutes) % 60
    return to_12_hours_format(str(hours) + ':' + str(minutes))

def day_diff(start, duration):
    _24_hours_format_start = to_24_hours_format(start)
    start_hour = int(_24_hours_format_start.split(':')[0])
    start_minute = int(_24_hours_format_start.split(':')[1])
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])
    return (start_hour + duration_hours + (start_minute + duration_minutes) // 60) // 24

def day_of_week(start_day, days_passed):
    days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    start_day_index = days_of_the_week.index(start_day)
    return days_of_the_week[(start_day_index + days_passed) % 7].capitalize()

def add_time(start, duration, start_day_of_week=''):
    time = add_time_to_start(start, duration)
    start_day_of_week = start_day_of_week.capitalize()
    if (start_day_of_week != ''):
        day_of_the_week = day_of_week(start_day_of_week, day_diff(start, duration))
        time += ', ' + day_of_the_week
    if day_diff(start, duration) == 1:
        time += ' (next day)'
    if day_diff(start, duration) > 1:
        time += f" ({day_diff(start, duration)} days later)"    
    return time

print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

# print(to_12_hours_format("31:10"))
# print(to_12_hours_format("11:43"))
# print(to_12_hours_format("100:10"))
# print(to_12_hours_format("11:43"))
# print(to_12_hours_format("6:30"))













