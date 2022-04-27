from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/rate', methods=['POST'])
def rate():
    energy = request.form['energy']
    time = request.form['time']
    transaction = request.form['transaction']

    meterStart = request.form['meterStart']
    timestampStart = request.form['timestampStart']
    meterStop = request.form['meterStop']
    timestampStop = request.form['timestampStop']
    
    timestampStart = datetime.datetime.now()
    timestampStop = datetime.datetime.now()

    return_dict = {
        "overall": energy,
        "components": {
            "energy": "444",
            "time": "555",
            "transaction": "666",
        }
    }

    return return_dict
  