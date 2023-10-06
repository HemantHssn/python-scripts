import pandas as pd

x = range(250000, 4000000 + 1, 50000)
data = []
for income in x:
    if income <= 500000:
        tax = 0.05 * (income - 250000)
    elif income <= 1000000:
        tax = 25000 + 0.2 * (income - 500000)
    else:
        tax = 112500 + 0.3 * (income - 1000000)
    data.append([income/100000, tax])

df = pd.DataFrame(data, columns=['Total Income (in lakh)', 'Tax (in Rupees)'])
df.to_excel('tax_data.xlsx', index=False)
