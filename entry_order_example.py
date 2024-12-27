from kiteconnect import KiteConnect
import datetime as dt
import time
import pandas as pd
import numpy as np
import os
access_token = open("access_token.txt",'r').read() #obtained access token was written to a file 'access_token.txt' in same folder


kite = KiteConnect(api_key='api_key')
kite.set_access_token(access_token)

# SIGNAL FOR STOCK
trade_matrix = {'internal_trade_id' : 123456,
                'entry_time': Timestamp('2024-12-26 10:33:00'),
                'tradingsymbol' : 'UJJIVANSFB',
                'enter_price' : 36.74,
                'stop_loss':36.44,
                'first_target':36.85,
                'second_target':36.88,
                'third_target':36.9,
                'fourth_target':36.95,
                'enter_qty': 4,
                'exit_qty_stop_loss': 4,
                'exit_qty_first_target': 1,
                'exit_qty_second_target': 1,
                'exit_qty_third_target': 1,
                'exit_qty_fourth_target': 1}


try:
    order_id = kite.place_order(tradingsymbol=trade_matrix['tradingsymbol'],
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=trade_matrix['enter_qty'],
                                variety=kite.VARIETY_REGULAR,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_MIS,
                                validity=kite.VALIDITY_DAY, 
                                tag = trade_matrix['int_trade_id'])
    time.sleep(2)
    print(kite.orders()[0]['status'])
except:
    print(order_id , kite.orders()[-1]['status_message'])

# SIGNAL FOR DERIVATIVES ie FUTURE OR OPTION - 
trade_matrix = {'internal_trade_id' : 135467,
                'entry_time': Timestamp('2024-12-26 09:33:00'),
                'tradingsymbol' : 'NIFTY24DEC23850PE',
                'enter_price': 61.5,
                'stopLoss': 35.6,
                'first_target': 87.4,
                'second_target': 113.2,
                'third_target': 139.1,
                'fourth_target': 165.0,
                'enter_qty': 100,
                'exit_qty_stop_loss': 100,
                'exit_qty_first_target': 25,
                'exit_qty_second_target': 25,
                'exit_qty_third_target': 25,
                'exit_qty_fourth_target': 25}

try:
    order_id = kite.place_order(tradingsymbol=trade_matrix['tradingsymbol'],
                                exchange=kite.EXCHANGE_NFO,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=trade_matrix['enter_qty'],
                                variety=kite.VARIETY_REGULAR,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_MIS,
                                validity=kite.VALIDITY_DAY, 
                                tag = trade_matrix['int_trade_id'])
    time.sleep(2)
    print(kite.orders()[0]['status']) # RESPONSE == 'COMPLETE'
except:
    print(order_id , kite.orders()[-1]['status_message']) # RESPONSE != COMPLETE (rejected/pending/put order req recieved etc see kite documentation)

