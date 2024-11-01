import yfinance as yf
import pandas as pd
import random 
from datetime import datetime
from dateutil.relativedelta import relativedelta

oggi = datetime.today()
ieri = oggi - relativedelta(day=1)
def get_random_titolo():
    x = (random.choice(open("Titoli.txt","r").readline().split()))
    return x

#stock_symbol = get_random_titolo()+".MI"
stock_symbol = 'STLA'
print(stock_symbol)

# Retrieve the historical price data using yfinance
stock_data = yf.download(stock_symbol, start='2024-10-21', end= '2024-11-01')
stock_data.columns = [col[0] for col in stock_data.columns]

def calculate_support_resistance(data):
    # Assicura che data sia un DataFrame e che le colonne esistano
    if not isinstance(data, pd.DataFrame) or not {'High', 'Low', 'Close'}.issubset(data.columns):
        raise ValueError("Il parametro 'data' deve essere un DataFrame con le colonne 'High', 'Low' e 'Close'.")

    # Calcola i livelli come Serie Pandas
    pivot_point = (data['High'] + data['Low'] + data['Close']) / 3
    support_l1 = (pivot_point * 2) - data['High']
    support_l2 = pivot_point - (data['High'] - data['Low'])
    resistance_l1 = (pivot_point * 2) - data['Low']
    resistance_l2 = pivot_point + (data['High'] - data['Low'])

    # Crea un DataFrame con le Serie calcolate
    support_resistance = pd.DataFrame({
        'Pivot': pivot_point,
        'Support_l1': support_l1,
        'Support_l2': support_l2,
        'Resistance_l1': resistance_l1,
        'Resistance_l2': resistance_l2
    }, index=data.index)
    
    return pivot_point, support_l1, support_l2, resistance_l1, resistance_l2, support_resistance

pivot_point, support_l1, support_l2, resistance_l1, resistance_l2, support_resistance = calculate_support_resistance(stock_data)

print(f"Pivot: {pivot_point}")
print(f"Support_l1: {support_l1}")
print(f"Support_l2: {support_l2}")
print(f"Resistance_l1: {resistance_l1}")
print(f"Resistance_l2: {resistance_l2}")

resistance_l2_mean = support_resistance['Resistance_l2'].mean()

print(f"Media Resistance_l2: {resistance_l2_mean}")

