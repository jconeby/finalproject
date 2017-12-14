import requests
import numpy as np

def currentRates():
    # create dictionary of exchange rates from fixer.io API
    exchange_rates = requests.get("https://api.fixer.io/latest?base=USD").json()
    exchange = exchange_rates['rates']


    # create Country List
    countrykey = exchange.keys()
    country = []

    for i in countrykey:
      country.append(i)

    # create Currency Value List
    values = exchange.values()
    exchange_values = []
    for i in values:
      exchange_values.append(i)
  
    # Create two columns showing data
    xarray = np.array(country)
    yarray = np.array(exchange_values)

    data = np.array([xarray, yarray])
    data = data.T
    return data
