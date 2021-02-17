from pycbrf.toolbox import ExchangeRates
from decimal import Decimal
from pytz import timezone
from datetime import datetime
import yfinance as yf
import requests


# Текущая дата
def get_now() -> str:
    moscow_tz = timezone("Europe/Moscow")
    return moscow_tz.localize(datetime.now()).strftime("%Y-%m-%d")

# Текущий курс доллара
def get_usd_course() -> Decimal:
    rates = ExchangeRates(get_now())
    return rates['USD'].value

def get_tsla_price() -> str:
    Tesla = yf.Ticker("TSLA")
    return Tesla.info['ask']

def get_apple_price() -> str:
    Apple = yf.Ticker("AAPL")
    return Apple.info['ask']

def get_btc_price():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print(get_usd_course())