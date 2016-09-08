from flask import Flask, render_template
from config import locations, port
from random import choice
from v1.sunset import isSunset

app = Flask(__name__)


@app.route('/')  # serve at root of website
def home():
    if isSunset():
        location = choice(locations)
        return render_template('base.html', location=location), 200
    else:
        return render_template('base.html', location="Try again later"), 403


if __name__ == '__main__':  # only run if this is being run as the main app
    app.run(port=port, debug=True)
