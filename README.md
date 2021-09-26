# CoinGecko API usage example
[![PyPi Version](https://img.shields.io/pypi/v/pycoingecko.svg)](https://pypi.python.org/pypi/pycoingecko/)
![GitHub](https://img.shields.io/github/license/man-c/pycoingecko)

Using the Python 3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3)

### Installation
PyPI
```bash
pip install pycoingecko
```
or from source
```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

### Examples
API documentation https://www.coingecko.com/en/api/documentation. On this site you can view detailed information as well as other HTTPS requests.

   **/coins/markets** (List all supported coins price, market cap, volume, and market related data)
   
    cg.get_coins_markets()
    
