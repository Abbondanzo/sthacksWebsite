from flask import Flask
import requests
import json
from datetime import datetime

app = Flask(__name__)


@app.route('/')  # serve at root of website
def home():
    time = getTimeOfSunset()  # get the time of the sunset
    # parse hours, minutes, and seconds from sunset time
    (sunset_hours, sunset_minutes, sunset_seconds) = tuple(
        time.replace(' PM', '').split(":"))
    (sunset_hours, sunset_minutes, sunset_seconds) = int(sunset_hours), int(
        sunset_minutes), int(sunset_seconds)  # make them all ints
    currentTime = datetime.now()  # get the current time
    (current_hours, current_minutes) = (currentTime.hour,
                                        currentTime.minute)
    # get the current hours, minutes, and seconds
    # sunset_hours = Chours # debugging
    # Cminutes = sunset_minutes - 5 # debugging
    # if PM (because sunset) and correct hour, and is wednesday
    if 'PM' in time and sunset_hours == current_hours and currentTime.isoweekday() == 3:
        if sunset_minutes - 10 < current_minutes < sunset_minutes:
            # if within 10 minutes of sthacks
            return "Sthacks!"
    else:
        return "No sthacks"


def getTimeOfSunset():  # returns time of sunset in the form of "11:33:27 PM"
    # hit up the API to get the time
    url = """
    http://api.sunrise-sunset.org/json?lat=42.340955&lng=-71.090507&date=today
    """
    get = requests.get(url)
    apiResp = json.loads(get.text)  # parse the JSON
    # return the time of sunset in the city
    return apiResp["results"]["civil_twilight_end"]

if __name__ == '__main__':  # only run if this is being run as the main app
    app.run(port=80)
