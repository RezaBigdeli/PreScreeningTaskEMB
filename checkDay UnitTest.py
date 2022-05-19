import datetime

dayList =("2022-05-19","2022:05:15")

def checkDay():
    today = datetime.datetime.now()
    for i in range(len(dayList)):
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



result = checkDay()
if result =="ok":
    print("The Alarm is for today: " ,datetime.datetime.now())
   
