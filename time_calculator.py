def add_time(start, duration,day=''):
  start_list = [str.split(':') for str in start.split(' ')]
  [adding_hour,adding_min] = duration.split(':')
  start_hour = start_list[0][0]
  start_min = start_list[0][1]
  start_period = start_list[1][0]
  added_hours = int(start_hour)+int(adding_hour)
  added_mins = int(start_min)+int(adding_min)
  added_hours+=(added_mins//60)
  added_mins = added_mins%60
  added_hours+=12 if start_period == 'PM' else 0
  added_days=added_hours//24
  added_hours=added_hours%24
  mins = added_mins
  hours = added_hours
  days = added_days
  period = 'PM' if hours > 11 else 'AM'
  hours-= 12 if hours > 12 else 0
  hours = 12 if hours == 0 else hours
  new_time = str(hours).format()+':'+str(mins).zfill(2)+' '+period
  print(new_time)
  message = ''
  if len(day)!=0:
    week = ['Sunday', 'Monday', 'Tuesday', 
            'Wednesday', 'Thursday', 'Friday', 
            'Saturday','Sunday', 'Monday', 'Tuesday', 
            'Wednesday', 'Thursday', 'Friday', 
            'Saturday']
    i = days % 7 if days > 7 else days
    start_index = week.index(day.capitalize())
    message += ', ' + week[start_index + i]
  if days == 0:
    message += ''
  elif days == 1:
    message += ' (next day)'
  else:
    message += ' (' + str(days) + ' days later)'
  new_time+= message
  return new_time
