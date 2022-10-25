import fyers_login
fyers = fyers_login.fyers

import pandas as pd
import datetime
import pytz

def historical_bydate(symbol, sd, ed, interval = 1):
    data = {"symbol":symbol, "resolution":"5", "date_format":"1", "range_from":str(sd),"range_to":str(ed),"cont_flag":str(interval)}
    nx = fyers.history(data)
    cols = ['datetime', 'open', 'high', 'low', 'close', 'volume']
    print(nx)
    df = pd.DataFrame.from_dict(nx['candles'])
    df.columns = cols
    df['datetime'] = pd.to_datetime(df['datetime'], unit = "s")
    df['datetime'] = df['datetime'].dt.tz_localize('utc').dt.tz_convert('Asia/Kolkata')
    df['datetime'] = df['datetime'].dt.tz_localize(None)
    df = df.set_index('datetime')
    return df

sd = datetime.date(2022, 10, 20)
enddate = datetime.datetime.now().date()
df = pd.DataFrame()

n = abs((sd - enddate).days)
ab = None
while ab == None:
    sd = (enddate - datetime.timedelta(days = n))
    ed = (sd + datetime.timedelta(days= 99 if n > 100 else n)).strftime("%Y-%m-%d")
    sd = sd.strftime("%Y-%m-%d")
    # dx = historical_bydate("NSE:NIFTYBANK-INDEX", sd, ed)
    dx = historical_bydate("NSE:BANKNIFTY22OCT41100CE", sd, ed)
    df = df.append(dx)
    n = n - 100 if n > 100 else n - n
    print(n)
    if n == 0:
        ab = "done"

df.to_csv(r"C:\temp\python-deploy\Historical data\BankNifty_5.csv")