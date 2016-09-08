from flask import Flask, render_template
from config import locations, port
from os import path, system
from random import choice
from v1.sunset import isSunset

app = Flask(__name__)


@app.route('/webbook/')
def webhookHandler():
    system("git pull")
    return "Ok", 200


@app.route('/')  # serve at root of website
def home():
    if isSunset():
        location = choice(locations)
        return render_template('base.html', info_location=location), 200
    else:
        return render_template('base.html', info_location="Try again later"), 403


if __name__ == '__main__':  # only run if this is being run as the main app
    if path.isfile('signed.crt') and path.isfile('domain.key'):  # if the real keys exist
        context = ('signed.crt', 'domain.key')
    else:
        context = ('selfSigned.crt', 'selfSigned.key')
    app.run(port=port, host='0.0.0.0', ssl_context=context, use_reloader=True)
