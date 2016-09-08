from flask import Flask, render_template
import requests
import json
from datetime import datetime
from config import locations, port
from random import choice

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
    # sunset_hours = current_hours # debugging
    # current_minutes = sunset_minutes - 5 # debugging
    # if PM (because sunset) and correct hour, and is wednesday
    if 'PM' in time and sunset_hours == current_hours and currentTime.isoweekday() == 3:
        if sunset_minutes - 10 < current_minutes < sunset_minutes:
            # if within 10 minutes of sthacks
            location = choice(locations)
            return render_template('base.html', location=location)
    else:
        return render_template('base.html', location="Try again later")


def getTimeOfSunset():  # returns time of sunset in the form of "11:33:27 PM"
    # hit up the API to get the time
    url = "http://api.sunrise-sunset.org/json?lat=42.340955&lng=-71.090507&date=today"
    get = requests.get(url)
    apiResp = json.loads(get.text)  # parse the JSON
    # return the time of sunset in the city
    return apiResp["results"]["civil_twilight_end"]

if __name__ == '__main__':  # only run if this is being run as the main app
    app.run(port=port, debug=True)
