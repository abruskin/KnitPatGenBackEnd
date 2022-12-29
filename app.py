from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
        return "<p>Hello, World! </p>"



###@app.post("/hat/beanietoque")
###def hat_beanie_toque():

@app.post("/gauge")
def get_gauge():
    request_data = request.get_json()
    stitchesInSwatch = request_data['stitchesInSwatch']
    swatchWidth = request_data['swatchWidth']
    rowsInSwatch = request_data['rowsInSwatch']
    swatchLength = request_data['swatchLength']
    swatchUnits = request_data['swatchunits']

    if swatchUnits == "inches":
        stitchesPerInch = int(stitchesInSwatch) / int(swatchWidth)
        rowsPerInch = int(rowsInSwatch) / int(swatchLength)
        return f"The gauge is {stitchesPerInch} stitches and {rowsPerInch} rows per inch. "
    else:
        stitchesPerCentimeter = int(stitchesInSwatch) / int(swatchWidth)
        rowsPerCentimeter = int(rowsInSwatch) / int(swatchLength)
        return f'The gauge is {stitchesPerCentimeter} stitches and {rowsPerCentimeter} rows per centimeter.'
