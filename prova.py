from datetime import datetime
from dateutil.relativedelta import relativedelta

# Data di oggi
data_oggi = datetime.today()

# Calcolo della data di oggi meno 6 mesi
data_meno_6_mesi = data_oggi - relativedelta(months=6)

print("Data di oggi:", data_oggi.strftime("%Y-%m-%d"))
print("Data di oggi meno 6 mesi:", data_meno_6_mesi.strftime("%Y-%m-%d"))
