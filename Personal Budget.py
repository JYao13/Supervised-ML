#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import requests
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


# In[2]:


# import the cost file - mastercard

month = '0719' # change this to applicable month

mc_file = r'C:\Users\jymas\Desktop\Personal\Official\Receipts\Monthly Bills\mc_' + month +'.csv'
df_costs = pd.read_csv(mc_file)

# filter for all expenses
df_costs = df_costs[df_costs['Activity Type'] != 'Payment']

total = round(df_costs['Amount'].sum(),2)


# In[3]:


# create summary df

df_summary = df_costs.groupby('Merchant Category Description', sort=False).sum().fillna(0)
df_summary = df_summary.sort_values(by=['Amount'], ascending=False)

sum_total = round(df_summary['Amount'].sum(),2)
check = abs(sum_total - total) < 0.1

if check:
    print('Passed')
else:
    raise Exception('Total Costs do not match: ' + str(abs(sum_total - total)) + ' - difference' )


# In[4]:


# summarize by day and week

df_summary['Week'] = df_summary['Amount'] / 4
df_summary['Day'] = df_summary['Week'] / 7

week_tot = round(df_summary['Week'].sum(), 2)
day_tot = round(df_summary['Day'].sum(), 2)
cat_set = list(dict.fromkeys(df_costs['Merchant Category Description'].tolist()))

print('Total: $' + str(total))
print('Week Total: $' + str(week_tot))
print('Day Total: $' + str(day_tot))

df_summary


# In[5]:


print(cat_set)


# In[34]:


# category filters

cat_filter = cat_set[0]

df_cat = df_costs[df_costs['Merchant Category Description'] == cat_filter].sort_values(by=['Amount'], ascending=False)


# In[35]:


df_cat


# In[36]:


df_cat.groupby('Merchant Name')['Amount'].sum()


# In[ ]:




