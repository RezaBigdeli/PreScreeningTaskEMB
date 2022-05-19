dayList =("2022-05-19","2022-05-19 ","2021-05-19","2022-19-05","2022-05-35","2022:05:19","2022/05/19")


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


for i in range(len(dayList)):
    alarm_day = dayList[i]
    result = validate_day(alarm_day)
    print(f"{dayList[i]}",result)
