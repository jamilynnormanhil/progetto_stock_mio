import yfinance as yf
import pandas as pd
import random 
  


def get_random_titolo():
    x = (random.choice(open("Titoli.txt","r").readline().split()))
    return x

stock_symbol = get_random_titolo()+".MI"
print(stock_symbol)
start_date = '2024-10-23'
end_date = '2024-10-24'

# Retrieve the historical price data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

def calculate_support_resistance(data):
    pivot_point = (data['High'] + data['Low'] + data['Close']) / 3
    support_l1 = (pivot_point * 2) - data['High']
    support_l2 = pivot_point - (data['High'] - data['Low'])
    resistance_l1 = (pivot_point * 2) - data['Low']
    resistance_l2 = pivot_point + (data['High'] - data['Low'])
    
    return pivot_point, support_l1, support_l2, resistance_l1, resistance_l2

pivot_point, support_l1, support_l2, resistance_l1, resistance_l2 = calculate_support_resistance(stock_data)

#DA FIXARE
#levels_data = pd.DataFrame({'Pivot Point': pivot_point,
#                            'Support Level 1': support_l1,
#                            'Support Level 2': support_l2,
#                            'Resistance Level 1': resistance_l1,
#                            'Resistance Level 2': resistance_l2})
