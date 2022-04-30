from flask import Flask, render_template, request, abort
from datetime import datetime

def create_app():
    app = Flask(__name__)
    return app

application = create_app()

@application.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@application.route('/rate', methods=['POST'])
def rate():
    if request.method == "POST":
        print("POST at /rate")

        try:    
            #rate
            energy = float(request.form.get("rate[energy]"))
            time = float(request.form.get("rate[time]"))
            transaction = float(request.form.get("rate[transaction]"))
            
            #cdr
            meterStart = int(request.form.get("cdr[meterStart]"))
            timestampStart = request.form.get("cdr[timestampStart]").replace('T', ' ')
            meterStop = int(request.form.get("cdr[meterStop]"))
            timestampStop = request.form.get("cdr[timestampStop]").replace('T', ' ')

            kwh = (meterStop - meterStart) / 1000
            hours = (datetime.strptime(timestampStop, "%Y-%m-%d %H:%M")-datetime.strptime(timestampStart, "%Y-%m-%d %H:%M")).total_seconds() / 3600.0
            output_dict = output(round(kwh*energy, 3), round(hours*time, 3), transaction)
            return output_dict
        except:
            abort(400)
    abort(400)

def output(energy, time, transaction):
    return {
        "overall" : round(transaction + energy + time, 2),
        "components" : {
            "energy" : energy,
            "time" : time,
            "transaction" : transaction
        }}
  