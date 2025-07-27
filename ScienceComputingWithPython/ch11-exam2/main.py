def add_time(start: str, duration: str, weekday: str=None) -> str:
    "Time Calc"

    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if weekday:
        # Get the index of the weekday
        week_index = weekdays.index(weekday.lower())
    
    # duration
    duration_list = [int(i) for i in duration.split(':')]
    duration_m = duration_list[0]*60 + duration_list[1]

    # AM
    if start.endswith('AM'):
        start_list = start.rstrip(' AM').split(':')
        start_list = [int(i) for i in start_list]
        start_m = start_list[0]*60 + start_list[1]

    # PM
    if start.endswith('PM'):
        start_list = start.rstrip(' PM').split(':')
        start_list = [int(i) for i in start_list]
        start_m = (12 + start_list[0])*60 + start_list[1]

    total = start_m + duration_m

    d = total // (24*60)
    h = (total - d *24 * 60) // 60
    m = '%02d' % (total % 60)
    # print(d, h, m)
    if d == 0:
        d_info = ''
    elif d == 1:
        d_info = ' (next day)'
    elif d > 1:
        d_info = f' ({d} days later)'

    if h == 0:
        h += 12
        suffix = 'AM'
    elif h <= 12:
        suffix = 'PM'
    elif h > 12:
        suffix = 'PM'
        h = h - 12
    time_info = f'{h}:{m} {suffix} '.strip()
    # print(time_info, d_info)
    

    if weekday:
        week_index = (week_index + d) % 7
        week_info = weekdays[week_index].title()

        new_time = time_info.strip() + ', ' + week_info + d_info
    else:
        new_time = time_info + d_info
    # print(d, h, m)
    print(new_time)
    return new_time

add_time('3:30 PM', '2:12') # '5:42 PM'.
add_time('11:55 AM', '3:12') # '3:07 PM'.
# 3. Expected time to end with '(next day)' when it is the next day.
# 4. Expected period to change from AM to PM at 12:00.
add_time('2:59 AM', '24:00') # '2:59 AM (next day)'.
add_time('11:59 PM', '24:05') # '12:04 AM (2 days later)'.
add_time('8:16 PM', '466:02') # '6:18 AM (20 days later)'.
# 8. Expected adding 0:00 to return the initial time.
add_time('3:30 PM', '2:12', 'Monday')# '5:42 PM, Monday'.
add_time('2:59 AM', '24:00', 'saturDay') # '2:59 AM, Sunday (next day)'.
add_time('11:59 PM', '24:05', 'Wednesday') # '12:04 AM, Friday (2 days later)'.
add_time('8:16 PM', '466:02', 'tuesday') # '6:18 AM, Monday (20 days later)'.

