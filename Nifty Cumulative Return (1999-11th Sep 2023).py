#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import python libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Yearly Nifty returns from 2000 to 2023

years = np.arange(1999, 2024)
annual_returns = [24.4, -13.4, -15.0, 5.3, 76.6, 13.0, 38.6, 41.9, 56.8, -51.3, 77.6, 19.2, -23.8, 29.4, 8.1, 32.9, -3.0, 4.4, 30.3, 4.6, 13.5, 16.1, 25.6, 5.7, 11.4]  # Random sample data

# Create a DataFrame
data = {'Year': years, 'Annual Return (%)': annual_returns}
df = pd.DataFrame(data)

# Calculate the cumulative return
df['Cumulative Return'] = (1 + df['Annual Return (%)']/100).cumprod() - 1

# Calculate the CAGR
years_passed = df['Year'].iloc[-1] - df['Year'].iloc[0]
cagr = (1 + df['Cumulative Return'].iloc[-1]) ** (1/years_passed) - 1

# Plotting the cumulative returns
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Cumulative Return'] * 100, marker='o')
plt.title('Nifty Cumulative Return (1999-2023*)')
plt.xlabel('Year')
plt.ylabel('Cumulative Return (%)')
plt.grid(True)
plt.show()


# In[4]:


# Calculate cumulative return in percentile

cagr * 100


# In[ ]:




