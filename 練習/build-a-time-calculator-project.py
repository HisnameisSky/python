def add_time(start, duration, starting_day=None):
    time_part, am_pm = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))
    
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    if am_pm == "PM" and start_hour != 12:
        start_hour += 12
    elif am_pm == "AM" and start_hour == 12:
        start_hour = 0
        
    total_minutes = start_hour * 60 + start_minute
    
    total_minutes += duration_hour * 60 + duration_minute

    days_later = total_minutes // 1440
    remaining_minutes = total_minutes % 1440
    
    new_hour = remaining_minutes // 60
    new_minute = remaining_minutes % 60
    
    if new_hour >= 12:
        new_am_pm = "PM"
        if new_hour > 12:
            new_hour -= 12
    else:
        new_am_pm = "AM"
        if new_hour == 0:
            new_hour = 12
            
    new_minute_str = str(new_minute).zfill(2)
    
    new_time = f"{new_hour}:{new_minute_str} {new_am_pm}"
    
    if starting_day:
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        starting_day = starting_day.lower().capitalize()
        start_day_index = days_of_week.index(starting_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"
        
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time