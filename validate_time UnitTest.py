timeList =("10:15:20 am","13:15:20 am","10:60:20 am","10:20:61 am","10:60:20  am","10:60:20")


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


for i in range(len(timeList)):
    alarm_time = timeList[i]
    result = validate_time(alarm_time)
    print(f"{timeList[i]}",result)
