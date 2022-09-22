import flask
from db_base import *
from base import *


app = flask.Flask(__name__)


@app.route("/get_filter_customers", methods=['GET'])
def get_filter_customers():
    base_control = DataBaseControl()
    city = flask.request.args.get('city')
    state = flask.request.args.get('state')
    filter = CustomerFilterFormat(city, state)
    query = filter.get_filtered_data()
    result = base_control.db_execute(query)
    result = filter.format_data(result)
    return result


@app.route("/get_names", methods=["GET"])
def first_names():
    base_control = DataBaseControl()
    format = FormatCounter()
    preresult = base_control.db_execute(format.get_data())
    result = format.format_data(preresult)
    return result


@app.route("/total_price", methods=["GET"])
def total_price():
    base_control = DataBaseControl()
    calculator = CalculatePriceFormat()
    query = calculator.get_data()
    result = calculator.calculate_format_price(base_control.db_execute(query))
    return result


app.run(debug=True)
