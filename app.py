from chalice import Chalice
import requests

app = Chalice(app_name='stock')

@app.route('/stock/{ticker}')
def stock(ticker):
    try:
        stock_data = get_stock_data(ticker)
        result_text = stock_data['ticker'] + ': ' + stock_data['price']
    except Exception as e:
        print e
        result_text = "Please enter in a valid ticker."
    return result_text

# Request from slack app
@app.route('/stock')
def slack_stock():
    try:
        stock_data = get_stock_data(app.current_request.query_params['text'])
        result_text = '''*{ticker}*
Price: {price}
Amt Change: {amt_change}
% Change: {perc_change}
Day High: {day_high}
Day Low: {day_low}'''.format(ticker=stock_data['ticker'],
                        price=stock_data['price'],
                        amt_change=stock_data['amt_change'],
                        perc_change=stock_data['perc_change'],
                        day_high=stock_data['day_high'],
                        day_low=stock_data['day_low']
                        )
    except Exception as e:
        print e
        result_text = "Please enter in a valid ticker. ie /stock xyz"
    return result_text

# Get price, amount change, percent change, day high, day low
def get_stock_data(ticker):
    url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + ticker + "&f=l1c1p2hg"
    values = requests.get(url).text.split(',')

    return {
        'ticker': ticker.upper(),
        'price': values[0],
        'amt_change': values[1],
        'perc_change': values[2].replace('"',''),
        'day_high': values[3],
        'day_low': values[4].replace('\n','')
        }
