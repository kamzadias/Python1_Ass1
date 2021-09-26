# CoinGecko API
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
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.\
**Any optional parameters** can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

For any parameter:
- ***Lists** are supported as input for multiple-valued comma-separated parameters\
  (e.g. see /simple/price usage examples).*
- ***Booleans** are supported as input for boolean type parameters; they can be `str` ('true', 'false'') or `bool` (`True`, `False`)\
  (e.g. see /simple/price usage examples).*

Usage examples:
```python
### API documentation
https://www.coingecko.com/api/docs/v3

### Endpoints included
> :warning: **Endpoints documentation**: To make sure that your are using properly each endpoint you should check the [API documentation](https://www.coingecko.com/api/docs/v3). Return behaviour and parameters of the endpoints, such as *pagination*, might have changed. <br> Any **optional parameters** defined in CoinGecko API doc can be passed as function parameters using same parameters names with the API *(see Examples above)*.
d_vs_currencies()
    ```
- *coins*
  - **/coins/markets** (List all supported coins price, market cap, volume, and market related data)
    ```python 
    cg.get_coins_markets()
    ```
