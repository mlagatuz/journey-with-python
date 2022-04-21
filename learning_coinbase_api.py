'''
Created on Apr 4, 2022

@author: mlagatuz

Saved API_{KEY,SECRET} as environmental variables
API_VERSION for Coinbase API: 2021-03-20 (Settings -> API -> API Version

I literally hacked up the coinbase-python python codebase, located at

    https://github.com/coinbase/coinbase-python

so I can learn http/api requests
'''

# my learning notes
# *args == parameters passed in as 'objects'
# **kwargs == parameters passed in as keyword arguments (kw=value)

# blob = response.json() 
# data = blob.get('data', None); default value is None

import json, os
from coinbase.wallet.client import Client

CB_API_KEY = os.getenv('CB_API_KEY')
CB_API_SECRET = os.getenv('CB_API_SECRET')
CB_API_VERSION = '2021-03-20'
BASE_API_URI = None

client = Client(CB_API_KEY, CB_API_SECRET, BASE_API_URI, CB_API_VERSION)

user = client.get_current_user()
user_as_json_string = json.dumps(user, indent=4)
print(user_as_json_string)

# Coinbase exchange rates
#cb_exchange_rates = client.get_exchange_rates()
#cb_exchange_rates_as_json_string = json.dumps(cb_exchange_rates, indent=4)
#print(cb_exchange_rates_as_json_string)

# Coinbase available currencies
#cb_available_currencies = client.get_currencies()
#cb_available_currencies_as_json_string = json.dumps(cb_available_currencies, indent=4)
#print(cb_available_currencies_as_json_string)

# Coinbase get buy price
#cb_buy_price = client.get_buy_price(currency_pair='SOL-USD')
#cb_buy_price_as_json_string = json.dumps(cb_buy_price, indent=4)
#print(cb_buy_price_as_json_string)

#cb_historical_prices = client.get_historic_prices(currency_pair='SOL-USD')
#cb_buy_price_as_json_string = json.dumps(cb_historical_prices, indent=4)
#print(cb_buy_price_as_json_string)

#cb_spot_price = client.get_spot_price(currency_pair='SOL-USD',date='2022-04-01')
#cb_spot_price_as_json_string = json.dumps(cb_spot_price, indent=4)
#print(cb_spot_price_as_json_string)

#cb_get_current_user = client.get_current_user()
#cb_get_current_user_as_json_string = json.dumps(cb_get_current_user, indent=4)
#print(cb_get_current_user_as_json_string)

#cb_user_id = '<Insert_User_Id>'
#cb_get_user = client.get_user(cb_user_id)
#cb_get_current_user_as_json_string = json.dumps(cb_get_user, indent=4)
#print(cb_get_user)

#cb_get_auth_info = client.get_auth_info()
#cb_get_auth_info_as_json_string = json.dumps(cb_get_auth_info, indent=4)
#print(cb_get_auth_info_as_json_string)

# https://developers.coinbase.com/api/v2#list-accounts
# This api call produces errors, used with Python-v3.9, maybe try with Pythonv3.6
#cb_get_all_accounts = client.get_accounts()
#cb_get_accounts_as_json_string = json.dumps(cb_get_all_accounts, indent=4)
#print(cb_get_accounts_as_json_string)

# https://developers.coinbase.com/api/v2#show-an-account
#cb_account_id = '<Insert_Account_Id'
#cb_btc_tx = client.get_account(cb_account_id)
#cb_btc_tx_as_json_string = json.dumps(cb_btc_tx, indent=4)
#print(cb_btc_tx_as_json_string)