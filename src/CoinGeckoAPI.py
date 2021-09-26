from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def functionTest(n):
    coinsMarket = cg.get_coins_markets(vs_currency = 'usd')

    x = 0

    coinsList = []
    for i in coinsMarket:
        coinsList.append(i["name"])
        if x == n-1:
            break
        x += 1

    return coinsList