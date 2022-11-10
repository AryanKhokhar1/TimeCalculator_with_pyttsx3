def add_time(start, duration):
    # Function that returns a specified time based on a start time, duration. Imports are not allowed.
    
    # Extract data from given start and duration strings.
    startArr = start.split(' ')
    startTime = startArr[0].split(':')
    ampm = 'AM'
    durationTime = duration.split(':')

    # Add the hours together from start and duration
    tmpEndHour = (int(startTime[0]) + int(durationTime[0]))

    # Add 12 hours to the temporary end hour in case 'PM'(so we can change timeline into 24 hours).
    if startArr[1] == 'PM':
        tmpEndHour += 12

    # Add the start and duration minutes together
    tmpEndMinute = (int(startTime[1]) + int(durationTime[1]))

    # If the sum of start time minute and duration time minute is greater than 59 add 1 hour to temporary end hour
    if(tmpEndMinute > 59):
        tmpEndHour += 1
    
    # Count the number of days that will have passed after the duration.
    days = int(tmpEndHour//24) # Flooring the division

    # Calculate the end hour using modulo in a 24h format.
    endHour = tmpEndHour % 24

    # Change the 'AM' to 'PM' if the 12th hours is passed.
    if endHour > 11:
        ampm = 'PM'

    # Convert back to 12h format ()
    if endHour > 12:
        endHour -= 12
    elif endHour == 0:
        endHour = 12

    # Calculate the ending minute using modulo.
    endMinute = tmpEndMinute % 60

    # Concatonate the first part of the string
    # Here zfill is used for add zeroes to untill word for reach specific length
    endTime = str(endHour) + ':' + str(endMinute).zfill(2) + ' ' + ampm

    
    # If the day has changed, add the correct string value
    if days > 1:
        endTime += ' (' + str(days) + ' days later)'
    elif days > 0:
        endTime += ' (next day)'

    return endTime
ans = add_time("02:00 PM", "30:10")
ans = "Time will be " + ans

import pyttsx3

engine = pyttsx3.init()

# setProperty function used for to set the property
engine.setProperty('rate',120) 
engine.setProperty('volume',10) 
voices = engine.getProperty('voices')    
# engine.setProperty('voice', voices[0].id
# engine.setProperty('voice', voices[2].id)
print(ans)
engine.say(ans)
engine.runAndWait()