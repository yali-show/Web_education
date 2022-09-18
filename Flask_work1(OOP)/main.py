import base
import flask
app = flask.Flask(__name__)


@app.route("/get_info", methods=['GET'])
def exchange_check():
    date = flask.request.args.get('date', default='01.12.2020')
    baseCurrency = flask.request.args.get('baseCurrency', default='USD')
    currency = flask.request.args.get('currency', default='UAH')
    bank = flask.request.args.get('bank', default='NB')
    data = base.Data(date, baseCurrency, currency, bank)
    parser = base.Parser(data)
    result = parser.main()
    return result


app.run(debug=True)
