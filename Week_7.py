# Stocks dictionary 
dict_of_stock_prices = {
    "TSLA": 800,
    "F": 100,
    "APPL": 130,
    "AMD": 85,
    "BA": 240,
    "SHOP": 1100,
    "SNOW": 230,
    "SQ": 250,
    "DAL": 46,
    "RCL": 88,
}

ticker_symbol = input("Enter ticker symbol ")
if ticker_symbol in  dict_of_stock_prices: 
    print("The price of the stock is " + ticker_symbol + " " + str(dict_of_stock_prices.get(ticker_symbol)))
else: 
    print("ticker symbol not found", ticker_symbol)




