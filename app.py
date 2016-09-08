from flask import Flask, render_template
import requests
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')  # serve at root of website
def home():
    time = getTimeOfSunset()  # get the time of the sunset
    (Shours,Sminutes,Sseconds) = tuple(time.replace(' PM', '').split(":"))  # parse hours, minutes, and seconds from sunset time
    (Shours,Sminutes,Sseconds) = int(Shours),int(Sminutes),int(Sseconds)  # make them all ints
    currentTime = datetime.now()  # get the current time
    (Chours, Cminutes, Cseconds) = (currentTime.hour, currentTime.minute, currentTime.second)  # get the current hours, minutes, and seconds
    #Shours = Chours # debugging
    #Cminutes = Sminutes - 5 # debugging
    if 'PM' in time and Shours == Chours and currentTime.isoweekday() == 3:  # if PM (because sunset) and correct hour, and is wednesday
        if Sminutes - 10 < Cminutes < Sminutes: # if within 10 minutes of sthacks
            return "Sthacks!"
    else:
        return "No sthacks"
    
def getTimeOfSunset():  # returns time of sunset in the form of "11:33:27 PM"
    get = requests.get("http://api.sunrise-sunset.org/json?lat=42.340955&lng=-71.090507&date=today")  # hit up the API to get the time
    apiResp = json.loads(get.text)  # parse the JSON
    return apiResp["results"]["civil_twilight_end"]  # return the time of sunset in the city
    
if __name__ == '__main__':  # only run if this is being run as the main app
    app.run(port=80)
                
