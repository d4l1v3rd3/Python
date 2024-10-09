investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = bitcoin_amount * bitcoin_value_usd
  return usd_value

invest = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if invest <= 30000:
  print("Bitcoin falls below $30,000")
else:
    print("worth $40,000")

