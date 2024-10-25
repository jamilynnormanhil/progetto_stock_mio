import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

italgas = yf.Ticker("IG.MI")
italgas.info
giorni_totali = italgas.shape[0]
periodo = int(total_days * 0.10) // 2
def identify_support_resistance(df, period):
    support_levels = []
    resistance_levels = []
    
    for i in range(period, len(df) - period):
        # Find the lowest low and highest high in the past '2*period' days centered around 'i'
        low_period = df['Low'][i-period:i+period+1].min()
        high_period = df['High'][i-period:i+period+1].max()
        
        # Check if the current low is the lowest low in the centered period
        if df['Low'][i] == low_period:
            support_levels.append((i, df['Low'][i]))
        
        # Check if the current high is the highest high in the centered period
        if df['High'][i] == high_period:
            resistance_levels.append((i, df['High'][i]))
    
    return support_levels, resistance_levels

# Identify support and resistance levels
support_levels, resistance_levels = identify_support_resistance(data, period)

# Print identified levels
print("Identified Support Levels (Index, Price):")
for level in support_levels:
    print(level)

print("\nIdentified Resistance Levels (Index, Price):")
for level in resistance_levels:
    print(level)
