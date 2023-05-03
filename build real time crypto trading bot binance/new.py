import ccxt.pro
from asyncio import run
from pprint import pprint

async def main():
    exchange = ccxt.pro.binance({"newUpdates": True})
    symbol = 'ETH/USDT'  # or BNB/USDT, etc...
    while True:
        try:
            trades = await exchange.watch_trades(symbol)
            # pprint(trades)
            ohlcvc = exchange.build_ohlcvc(trades, '1m')
            print(ohlcvc)
        except Exception as e:
            print(e)
            # stop the loop on exception or leave it commented to retry
            # raise e



run(main())