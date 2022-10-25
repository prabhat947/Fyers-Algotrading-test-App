from turtle import begin_fill
from fyers_api import fyersModel
from fyers_api import accessToken
import os
# Section Begin: Move to other py
from TickData import TickData
# Section End

app_id = 'KUF8RGNT3M-100'
app_secret = '4DS3G22BYI'

redirect_url = 'https://www.google.com/'

# app_id = 'M6C8ERZ7XN-100'
# app_secret = 'FFNRO20C3E'

# redirect_url = 'http://localhost:8080/apis/broker/login/fyers'


def get_access_token():
	if not os.path.exists("access_token.txt"):
		session =	accessToken.SessionModel(client_id=app_id,
					secret_key=app_secret,redirect_uri=redirect_url, 
					response_type="code", grant_type="authorization_code")
		response = session.generate_authcode()  
		print("Login Url : " + response)
		auth_code = input("Enter Auth Code : ")
		"""
		eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NjEwOTYyMTEsImV4cCI6MTY2MTEyNjIxMSwibmJmIjoxNjYxMDk1NjExLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUDE1MTg0Iiwibm9uY2UiOiIiLCJhcHBfaWQiOiJLVUY4UkdOVDNNIiwidXVpZCI6IjZlYjZjNmJlYzA5ZDRkMWQ4YWYyYTVkNDc1ODhjYWNmIiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.c88UhPcOWOzpdQfE6HpLPyxD25fkVfXxtuFxmsx3Jxc
		"""
		print("Auth Code: " + auth_code)
		session.set_token(auth_code)
		access_token = session.generate_token()["access_token"]
		print("access_token = " + access_token)
		with open("access_token.txt","w") as f:
			f.write(access_token)
	else:
		with open("access_token.txt","r") as f:
			access_token = f.read()
	return access_token

fyers = fyersModel.FyersModel(client_id=app_id, token=get_access_token(),log_path="C:\Prabhat\Learning\Vwap and Rsi Strategy Algo  Santosh  Live Algo Trading\logs")

# print(fyers.holdings())
# print(fyers.orderbook())

# orderId = "2220916421873"
# data = {"id":orderId}
# print(fyers.orderbook(data=data))

# print(fyers.market_status())

# print(fyers.holdings())
# def ohlc(name):
#     return {"symbol":"NSE:" + name + "-EQ","ohlcv_flag":"1"}

# data = {"symbol":"NSE:SBIN-EQ","resolution":"1","date_format":"0","range_from":"1622097600","range_to":"1622097685","cont_flag":"1"}
# print(fyers.history(data))

# data = {"symbols":"NSE:SBIN-EQ"}
# print(fyers.quotes(data))

# data = {"symbol":"NSE:SBIN-EQ","ohlcv_flag":"1"}
# print(fyers.depth(data))

# UNCOMMENT BELOW CODE FOR WEBSOCKET

from fyers_api.Websocket import ws


def run_process_foreground_symbol_data(access_token):
    '''This function is used for running the symbolData in foreground 
    1. log_path here is configurable this specifies where the output will be stored for you
    2. data_type == symbolData this specfies while using this function you will be able to connect to symbolwebsocket to get the symbolData
    3. run_background = False specifies that the process will be running in foreground'''
    data_type = "symbolData"
    # symbol = ["NSE:SBIN-EQ","NSE:ONGC-EQ"]   ##NSE,BSE sample symbols
    symbol =["MCX:CRUDEOIL22NOVFUT","NSE:NIFTY50-INDEX","NSE:NIFTYBANK-INDEX","NSE:SBIN-EQ","NSE:HDFC-EQ","NSE:IOC-EQ"]
    # symbol =["NSE:NIFTY50-INDEX","NSE:NIFTYBANK-INDEX"]
    # symbol =["MCX:SILVERMIC21NOVFUT","MCX:GOLDPETAL21SEPTFUT"]
    access_token1 = app_id + ":" + get_access_token()
    print('access_token1 = ' + access_token1)
    fs = ws.FyersSocket(access_token=access_token1,run_background=False,log_path="C:/temp/python-deploy/logs/")
    fs.websocket_data = custom_message
    fs.subscribe(symbol=symbol,data_type=data_type)
    fs.keep_running()


def run_process_foreground_order_update(access_token):
    '''This function is used for running the order_update in background 
    1. log_path here is configurable this specifies where the output will be stored for you.
    2. data_type == orderUpdate this specfies while using this function you will be able to connect to orderwebsocket to get the orderUpdate
    3. run_background = False specifies that the process will be running in foreground '''
    data_type = "orderUpdate"
    fs = ws.FyersSocket(access_token=access_token,run_background=False,log_path="C:/temp/python-deploy/logs/")
    fs.websocket_data = custom_message
    fs.subscribe(data_type=data_type)
    fs.keep_running()



def custom_message(msg):
    # print (f"Custom:{msg}") 
    on_ticks(msg)

# Section begin
def on_ticks(brokerTicks):
    # convert broker specific Ticks to our system specific Ticks (models.TickData) and pass to super class function
    ticks = []
    # bTick
    # {'symbol': 'MCX:CRUDEOIL22NOVFUT', 'timestamp': 1666279895, 
    # 'fyCode': 7208, 'fyFlag': 2, 'pktLen': 200, 'ltp': 7108.0, 
    # 'open_price': 7074.0, 'high_price': 7237.0, 'low_price': 7057.0, 'close_price': 7047.0, 
    # 'min_open_price': 7110.0, 'min_high_price': 7113.0, 'min_low_price': 7108.0, 'min_close_price': 7108.0, 
    # 'min_volume': 18, 'last_traded_qty': 2, 'last_traded_time': 1666279894, 'avg_trade_price': 714840, 
    # 'vol_traded_today': 24488, 'tot_buy_qty': 570, 'tot_sell_qty': 655, 
    # 'market_pic': [{'price': 7107.0, 'qty': 2, 'num_orders': 1}, 
    # {'price': 7106.0, 'qty': 3, 'num_orders': 3}, {'price': 7105.0, 'qty': 3, 'num_orders': 3}, 
    # {'price': 7104.0, 'qty': 5, 'num_orders': 5}, {'price': 7103.0, 'qty': 2, 'num_orders': 2}, 
    # {'price': 7108.0, 'qty': 3, 'num_orders': 2}, {'price': 7109.0, 'qty': 7, 'num_orders': 5}, 
    # {'price': 7110.0, 'qty': 7, 'num_orders': 4}, {'price': 7111.0, 'qty': 72, 'num_orders': 10}, 
    # {'price': 7112.0, 'qty': 3, 'num_orders': 2}]}
    for bTick in brokerTicks:
    #   isd = Instruments.getInstrumentDataByToken(bTick['instrument_token'])
    #   tradingSymbol = isd['tradingsymbol']
    #   tick = TickData(tradingSymbol)
      
      tick = TickData(bTick['symbol'])
      tick.lastTradedPrice = bTick['ltp']
      tick.lastTradedQuantity = bTick['last_traded_qty']
      tick.avgTradedPrice = bTick['avg_trade_price']
      tick.volume = bTick['vol_traded_today']
      tick.totalBuyQuantity = bTick['tot_buy_qty']
      tick.totalSellQuantity = bTick['tot_sell_qty']
      tick.open = bTick['open_price']
      tick.high = bTick['high_price']
      tick.low = bTick['low_price']
      tick.close = bTick['close_price']
    #   print("ltp: " + bTick['vol_traded_today'])
    #   print("ltp: " + bTick['ltp'])
      print("ltp:")
      print(tick.lastTradedPrice)
      ticks.append(tick)

    # for ticker in ticks:
    #     print(ticker)
# Section End

def main():
    ### Insert the accessToken and app_id over here in the following format (APP_ID:access_token) 
    access_token = app_id + ":" + get_access_token()

    ## run a specific process you need to connect to get the updates on
    run_process_foreground_symbol_data(access_token)

    # run_process_foreground_order_update(access_token)
    
if __name__ == '__main__':
	main()

