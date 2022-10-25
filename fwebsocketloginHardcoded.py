from fyers_api.Websocket import ws
from TickData import TickData

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
    
    fs = ws.FyersSocket(access_token=access_token,run_background=False,log_path="C:/temp/python-deploy/logs/")
    fs.websocket_data = custom_message
    fs.subscribe(symbol=symbol,data_type=data_type)
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

def main():
    ### Insert the accessToken and app_id over here in the following format (APP_ID:access_token) 
    # access_token = 'KUF8RGNT3M-100:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NjY0MTg1NDYsImV4cCI6MTY2NjQ4NTAyNiwibmJmIjoxNjY2NDE4NTQ2LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCalU0ZHlvbUZ4NDhTbFV1RUlXMDFWTkUxaG81OXU5V3JtOVBVRDZkQzdLMGRyTXVnOS1LY1RRYXg5T0VTUjBOVUc1WEZxczhqX0F5MjFhRmdMeG13dE5Pa0l6U1VndDF2U1dXazZRZWQ3OGxGNFp3dz0iLCJkaXNwbGF5X25hbWUiOiJQUkFCSEFUIFRJV0FSSSIsImZ5X2lkIjoiWFAxNTE4NCIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.5nPSzs7tj6rM4B2b6zvEUNlhbv8qmn29QsR4FOSdrsI'
    access_token = 'KUF8RGNT3M-100:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2NjY0Mzc2MDQsImV4cCI6MTY2NjQ4NTAwNCwibmJmIjoxNjY2NDM3NjA0LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCalU5SGtGVlhuUnhjeW9YckE3Yy1Yb2VRbU9SREpjWEhjdVFpZWNoWXA0NllkTlp3SGdTNVYzVnBKbHBSLURDRzRDSzRqYzhXMVlfWm5SeFhnb3hkeTBmYmRmQmdNYzFvRjAyY3hXM1hvVDA1X2E1ND0iLCJkaXNwbGF5X25hbWUiOiJQUkFCSEFUIFRJV0FSSSIsImZ5X2lkIjoiWFAxNTE4NCIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.8mfVhiyLwnpPCdASCts5BFm2Vi0PBm7MqZDSlRmE3HM'
    # access_token = 'M6C8ERZ7XN-100:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE2NjY0Mzc0OTIsImV4cCI6MTY2NjQ2NzQ5MiwibmJmIjoxNjY2NDM2ODkyLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUDE1MTg0Iiwibm9uY2UiOiIiLCJhcHBfaWQiOiJNNkM4RVJaN1hOIiwidXVpZCI6IjQ5NTFjNjMyN2M1NTQ1YmY4NDA1MDUxNDUzYzQ1ZTBhIiwiaXBBZGRyIjoiMC4wLjAuMCIsInNjb3BlIjoiIn0.Qgns-SkDM70OY0PWsKqF_RP6qJ6z2eSVBLMeZ8wfD_Q'

    ## run a specific process you need to connect to get the updates on
    run_process_foreground_symbol_data(access_token)

    # run_process_foreground_order_update(access_token)
    
if __name__ == '__main__':
	main()
