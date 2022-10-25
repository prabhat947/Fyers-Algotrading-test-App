import fyers_login
from fyers_api.Websocket import ws
# import tradehull_lib
# import pdb

fyers = fyers_login.fyers
with open("access_token.txt","r") as f:
	access_token = f.read()
print(access_token)

# watchlist = ['BPCL', 'MOTHERSUMI', 'RBLBANK', 'SIEMENS', 'GODREJPROP', 'CANBK', 'MARICO', 'BEL', 'NAVINFLIOR', 'TCS', 'LICHSGFIN']

# print(fyers.margins())
# for name in watchlist:
# 	#df = dataframe
# 	df = tradehull_lib.get_hist_data(name = name, exchange = 'NSE:', interval = '3minute', delta = 10, continuous = False, oi = False)
# 	pdb.set_trace()

def run_process_background_order_update(access_token):
    data_type = "orderUpdate"
    fs = ws.FyersSocket(access_token=access_token,run_background=True,log_path="C:\Prabhat\Learning\Vwap and Rsi Strategy Algo  Santosh  Live Algo Trading\logs\Tickers")
    fs.websocket_data = custom_message('SBIN')
    fs.subscribe(data_type=data_type)
    
    fs.keep_running()

def custom_message(msg):
    print (f"Custom:{msg}") 

print(access_token)
# access_token= "L9*****BW-100:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9******************************lcnMuaW4iLCJpYXQiOjE2MzE1ODY2MzUsImV4cCI6MTYzMTY2NTgzNSwibmJmIjoxNjMxNTg2NjM1LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCaFFBbExjOTlIUG85TTF4LWl5bTBZRFRHMHhXSi1HVGRkNU5BWlFET2xXYUpIS2h4S2RjMXVYckthc1R3VGlDQ01sYTBhanp6SmYwSWtHSHVFQjcwTThUcFcxckctQUdOWGZlQWhzZVY0bTVRSm1FRT0iLCJkaXNwbGF5X25hbWUiOiJQSVlVU0ggUkFKRU5EUkEgS0FQU0UiLCJmeV9pZCI6IkRQMDA0MDQiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.Dacrm4oZU1Vcarr3nW8rKueJpVNBJCNVvdjg0cDMQrQ"
# run_process_background_order_update(access_token)