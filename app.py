from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/rate', methods=['POST'])
def rate():
    #rate = request.get_json()#['rate']
    cdr = request.form

    print(cdr)
    #print(rate)
    #energy_consumed = cdr["meterStart"] - crd["meterStop"]

    return output( 1,2,3,4)

def output(overall, energy, time, transaction):
    return {
        "overall" : overall,
        "components" : {
            "energy" : energy,
            "time" : time,
            "transaction" : transaction
        }}
  