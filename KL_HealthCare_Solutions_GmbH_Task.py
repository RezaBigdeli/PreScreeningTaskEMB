from time import sleep
import datetime

timeList = list()
dayList = list()
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"

def validate_day(alarm_day):
    if len(alarm_day) != 10:
        return "Invalid format! Please try again..."
    else:
        if int(alarm_day[0:4])> 2100 or int(alarm_day[0:4]) < 2022:
            return "Invalid YEAR format! Please try again..."
        elif int(alarm_day[5:7]) > 12:
            return "Invalid MONTH format! Please try again..."
        elif int(alarm_day[8:10]) > 31:
            return "Invalid DAY format! Please try again..."
        else:
            return "ok"







while True:

    Number = int(input("Number of adjustment times: "))
    for i in range(Number):
        alarm_day = input("Enter Day in 'YYYY-MM-DD' format: ")
        alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
        validate = validate_time(alarm_time.lower())
        if validate != "ok":
            print(validate)
        validate = validate_day(alarm_day.lower())
        if validate != "ok":
            print(validate)
        else:
            dayList.append(alarm_day)
            timeList.append(alarm_time)
            print(f"Setting alarm for {alarm_time} {alarm_day}...")
    break

def checkDay():
    today = datetime.datetime.now()
    for i in range(Number):
        alarm_date = dayList[i]
        alarm_year = alarm_date[0:4]
        alarm_month = alarm_date[5:7]
        alarm_day = alarm_date[8:10]
        current_year = today.year
        current_month = today.strftime("%m")
        current_day = today.strftime("%d")
        if int(alarm_year) == int(current_year) :
            if int(alarm_month) == int(current_month) :
                if int(alarm_day) == int(current_day) :
                    return "ok"
                





def checkAlarm():
    validate = checkDay()
    if validate == "ok" :
        for i in range(Number):
            alarm_time = timeList[i]
            alarm_hour = alarm_time[0:2]
            alarm_min = alarm_time[3:5]
            alarm_sec = alarm_time[6:8]
            alarm_period = alarm_time[9:].upper()
            now = datetime.datetime.now()
            current_hour = now.strftime("%I")
            current_min = now.strftime("%M")
            current_sec = now.strftime("%S")
            current_period = now.strftime("%p")
            if alarm_period == current_period:
                if alarm_hour == current_hour:
                    if alarm_min == current_min:
                        if alarm_sec == current_sec:
                            print(f"The {i+1}st date has been reached!({dayList[i]} {alarm_time})")
                            sleep(1)


while True:

    
    checkAlarm()
