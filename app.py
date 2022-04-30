from flask import Flask, render_template, request, abort
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/rate', methods=['POST'])
def rate():
    if request.method == "POST":
        print("POST at /rate")
        
        #rate
        energy = request.form.get("rate[energy]")
        time = request.form.get("rate[time]")
        transaction = float(request.form.get("rate[transaction]"))

        #cdr
        meterStart = request.form.get("cdr[meterStart]")
        timestampStart = request.form.get("cdr[timestampStart]")
        meterStop = request.form.get("cdr[meterStop]")
        timestampStop = request.form.get("cdr[timestampStop]")

        overall = transaction

        output_dict = output(overall,2,3,transaction)
        return output_dict

    abort(400)

def output(overall, energy, time, transaction):
    return {
        "overall" : overall,
        "components" : {
            "energy" : energy,
            "time" : time,
            "transaction" : transaction
        }}
  