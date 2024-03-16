def add_time(start, duration, start_day=None):
    # splitting up input
    start_time, start_period = start.split()

    # storing variables from input
    start_hour = int(start_time.split(':')[0])
    start_hour %= 12
    start_min = int(start_time.split(':')[1])
    duration_hour = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])

    if duration_hour == 0 and duration_min == 0:
        return start

    # calculate total minutes
    total_minutes = start_hour * 60 + start_min
    if start_period == 'PM':
        total_minutes += 12 * 60

    total_minutes += duration_hour * 60 + duration_min

    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)

    new_hour = remaining_minutes // 60
    new_minute = remaining_minutes % 60

    if new_hour < 12 or new_hour == 24:
        new_period = 'AM'
    else:
        new_period = 'PM'

    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour -= 12

    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    if start_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days_of_week.index(start_day.lower().capitalize())
        new_day_index = (start_day_index + days) % 7

        new_day = days_of_week[new_day_index]
        if days == 1 and remaining_minutes >= 12 * 60:
            new_time += f", {new_day} (next day)"
        else:
            new_time += f", {new_day}"

    if days == 1 and remaining_minutes < 12 * 60:
        new_time += " (next day)"
    elif days >= 1:
        new_time += f" ({days} days later)"

    return new_time


print(add_time('3:30 PM', '2:12'))
print(add_time('11:55 AM', '3:12'))
print(add_time('2:59 AM', '24:00'))
print(add_time('11:59 PM', '24:05'))
print(add_time('8:16 PM', '466:02'))
print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
print(add_time('11:59 PM', '24:05', 'Wednesday'))
print(add_time('8:16 PM', '466:02', 'tuesday'))