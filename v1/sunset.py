import requests
import json
from datetime import datetime
from pytz import timezone

url = "http://api.sunrise-sunset.org/json?lat=42.340955&lng=-71.090507&date=today"


def getTimeOfSunset():  # returns time of sunset in the form of "11:33:27 PM"
    # hit up the API to get the time
    get = requests.get(url)
    apiResp = json.loads(get.text)  # parse the JSON
    # return the time of sunset in the city
    return apiResp["results"]["civil_twilight_end"]


def isSunset():
    time = getTimeOfSunset()  # get the time of the sunset
    (sunset_hours, sunset_minutes, sunset_seconds) = tuple(
        time.replace(' PM', '').split(":"))
    (sunset_hours, sunset_minutes, sunset_seconds) = int(sunset_hours), int(
        sunset_minutes), int(sunset_seconds)  # make them all ints
    currentTime = datetime.now().replace(tzinfo=timezone('UTC'))
    (current_hours, current_minutes) = (currentTime.hour,
                                        currentTime.minute)
    show_time = sunset_minutes - 10 < current_minutes < sunset_minutes
    is_evening = 'PM' in time
    same_hours = sunset_hours == current_hours
    is_wednesday = currentTime.isoweekday() == 3
    print('- ' * 20)
    print(show_time)
    print(current_minutes)
    print(sunset_minutes)
    print(is_evening)
    print(same_hours)
    print(is_wednesday)
    print('- ' * 20)
    return show_time and is_evening and same_hours and is_wednesday
