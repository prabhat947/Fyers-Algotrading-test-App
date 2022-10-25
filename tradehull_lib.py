from pkg_resources import to_filename
import fyers_login
import datetime
import pandas as pd

fyers = fyers_login.fyers

step_value = {'AARTIIND':20, 'ABBOTINDIA': 250}

def ohlc(name):

    data = fyers_login.ohlc(name)
    print(fyers.depth(data))
    openx = data[name]['ohlc']['o']
    high = data[name]['ohlc']['h']
    low = data[name]['ohlc']['l']
    close = data[name]['ohlc']['c']

    return openx, high, low, close

ohlc("SBIN")
"""
def option_name_finder(name, exp, ce_pe, multiplier):
    # opt_name = tl.option_name_finder(name = 'ACC', exp = '22AUG', ce_pe = 'CE', multiplier = steps)

    ltp = fyers.ltp(['NSE:' + name])['NSE:' + name]['last_price']
    script_step = step_value[name]
    #MISSED CODE HERE
    return option_name
"""

def get_hist_data(name, exchange, interval, delta, continuous, oi):
    to_date = datetime.datetime.now().date()
    from_date = to_date - datetime.timedelta(days=delta)
    token = fyers.ltp([exchange + name])[exchange + name]['instrument_token']
    data = fyers.historical_data(instrument_token=token, from_date=from_date, to_date=to_date, interval=interval, delta=delta, continuous=continuous, oi=oi)
    df = pd.DataFrame(data)
    #df = df.set_index(df['date'])
    return df