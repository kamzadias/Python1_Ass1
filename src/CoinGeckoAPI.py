from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

coinsMarket = cg.get_coins_markets(vs_currency = 'usd')

x = 0
n = int(input("Enter number of coins : "))

coinsList = []
for i in coinsMarket:
    coinsList.append(i["name"])
    if x == n-1:
        break
    x += 1

print(coinsList)