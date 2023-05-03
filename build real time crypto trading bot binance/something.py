import ccxt.pro
from asyncio import run
from pprint import pprint

async def main():
    exchange = ccxt.pro.binance({"newUpdates": True})
    symbol = "ETH/USDT"  # or BNB/USDT, etc...
    while True:
        try:
            candles = await exchange.watch_ohlcv(symbol)
            print(exchange.iso8601(exchange.milliseconds()), candles)
        except Exception as e:
            print(e)
            # stop the loop on exception or leave it commented to retry
            # raise e


run(main())
