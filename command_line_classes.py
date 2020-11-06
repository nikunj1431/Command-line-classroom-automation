def get_day(day,time):#This function returns the class we have given the day and the time range
    schedule = {"Monday":{"8:00 AM - 8:30 AM":"PE","8:45 AM - 9:00 AM":"CT", "10:00 AM - 10:45 AM":"Mathematics", "11:00 AM - 11:45 AM":"English",
                          "3:00 AM - 3:45 AM":"Chemistry"},
                "Tuesday":{"8:45 AM - 9:00 AM":"CT","9:00 AM - 9:45 AM":"Geography", "10:00 AM - 10:45 AM":"Physics", "11:00 AM - 11:45 AM":"Hindi"},
                "Wednesday":{"8:00 AM - 8:30 AM":"PE","8:45 AM - 9:00 AM":"CT", "10:00 AM - 10:45 AM":"Biology", "11:00 AM - 11:45 AM":"History",
                          "12:00 Noon - 12:45 PM":"Chemistry","3:00 PM - 3:45 PM": "6th Subject"},
                "Thursday": {"8:45 AM - 9:00 AM": "CT", "10:00 AM - 10:45 AM": "Mathematics","11:00 AM - 11:45 AM": "English",
                             "12:00 Noon - 12:45 PM": "History & Civics","3:00 PM - 3:45 PM":"6th Subject"},
                "Friday":{"8:45 AM - 9:00 AM":"CT","9:00 AM - 9:45 AM":"Geography", "10:00 AM - 10:45 AM":"Physics", "11:00 AM - 11:45 AM":"Hindi",
                           "12:00 Noon - 12:45 PM": "Biology"}
                }
    for i in schedule:
        if i == day:
            k = (schedule[i])
            class_right_now = k[time]
            print(class_right_now)






