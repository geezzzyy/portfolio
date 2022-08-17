#!/usr/bin/env python
# coding: utf-8

# ### Library Import

# In[628]:


#!pip install quantstats
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import quantstats as qs


# ### Creating the Equal Weighting Function

# In[629]:


def eq_weight(*args):
    
    ## Getting stock/portfolio data from yahoo
    stocks = [*args]
    data = yf.download(" ".join(stocks), start="2013-07-01", end="2022-07-01", interval = "1d", group_by = 'ticker')
    
    ## Data Preview
    data.head()
    len(data)
    
    ## Showing just Adj Closed values
    columns = []
    for x in stocks:
        y = (x, 'Adj Close')
        columns.append(y)
    
    data = data[columns]
    
    ## Drop NA values
    data = data.dropna(axis=0)
    
    
    ## Calculating Returns
    data_return = data.diff()/ data.shift() # Return table
    
    ## Naming the Returns Column
    return_columns = []
    
    for x in stocks:
        y = x + " % change"
        return_columns.append(y)
    
    data_return.columns = return_columns
    
    ## Calculating daily Average return amongst stocks and creating average return column
    data_return['daily average return'] = data_return.mean(axis = 1)
    
    
   
    
    ## Calculating the Returns over the years in dollars $$$
    data_return['Dollar Return'] = [0] * len(data_return)
    
    data_return.iloc[0,-1]= 100000 #setting starting capital as $100,000
    
    for i in range(1, len(data_return)):
        data_return.iloc[i, -1] = data_return.iloc[i-1, -1] * (1 + data_return.iloc[i, -2]) #(dollar return = capital * (1 + %change))
    
    
    ## Function Output
    print(f'final return: ${data_return.iloc[-1,-1]} ') # Last Portfolio Value-- July 1st 2022
    
    print(f'Sharpe ratio: ${qs.stats.sharpe(data_return.iloc[:,-1])} ') #Sharpe Ratio
   
    return plt.plot(data_return.iloc[:,-1])               # Plot

    
         


# ## IMPORTANT NOTE:
# The portfolios have varying start dates depending on when yahoo finance has
# data on every security in the portfolio. Adjust the start date from the function above

# # 1. Golden Butterfly Portfolio

# In[630]:


eq_weight('SHY', 'TLT', 'VTI', 'IWN', 'GLD')


# # 2. Rob Armott Portfolio

# In[631]:


eq_weight('BNDX', 'LQD', 'VEU', 'VNQ', 'SPY', 'TLT', 'TIP', 'DBC')


# # 3. Global Asset Allocation Portfolio

# In[632]:


eq_weight('SPY', 'EFA', 'EEM', 'LQD', 'BNDX', 'TLT', 'TIP', 'DBC','GLD', 'VNQ' )


# # 4. Permenant Portfolio

# In[633]:


eq_weight('BIL', 'GLD','SPY', 'TLT')


# # 5. Desert Portfolio

# In[634]:


eq_weight('IEF', 'VTI', 'GLD')


# # 6. The Larry Portfolio

# In[635]:


eq_weight('IWN', 'DLS', 'EEM', 'IEF')


# # 7. Big Rocks Portfolio

# In[636]:


eq_weight('AGG', 'SPY', 'IWD', 'IWM', 'IWN', 'EFV', 'VNQ', 'EFA', 'SCZ', 'DLS', 'EEM')


# # 8. Sandwich Portfolio

# In[637]:


eq_weight('IEF', 'SPY', 'SCZ', 'IWM', 'EEM', 'EFA', 'VNQ', 'BIL')


# # 9. Balanced Tax Aware Portfolio

# In[638]:


eq_weight('AGG', 'BIL', 'EFA', 'IWM', 'SPY', 'DBC', 'VNQ', 'EEM')


# # 10. Balanced Portfolio

# In[639]:


eq_weight('AGG', 'BIL', 'EFA', 'IWM', 'SPY', 'DBC', 'VNQ', 'EEM', 'TIP', 'BNDX', 'HYG')


# # 11. Income with Growth Portfolio

# In[640]:


eq_weight('AGG', 'BIL', 'EFA', 'IWM', 'SPY', 'DBC', 'VNQ', 'TIP', 'BNDX', 'HYG')


# # 12. Income Growth Tax Portfolio

# In[641]:


eq_weight('AGG', 'BIL', 'EFA', 'IWM', 'SPY', 'DBC', 'VNQ')


# # 13. Conservative Income Portfolio

# In[642]:


eq_weight('AGG', 'BIL', 'TIP', 'HYG', 'BNDX', 'VNQ')


# # 14. Conservative Income Tax Portfolio

# In[643]:


eq_weight('AGG', 'BIL', 'VNQ')


# # 15. All Weather Portfolio

# In[644]:


eq_weight('SPY', 'TLT', 'IEF', 'GLD', 'DBC')


# # 16. United Stated 60/40 Portfolio

# In[645]:


eq_weight('SPY', 'IEF')


# # 17. Ivy Portfolio Timing

# In[646]:


eq_weight('VTI', 'VEU', 'AGG', 'DBC', 'VNQ')


# # 18. Robust Asset Allocation Balanced

# In[647]:


eq_weight('IEF', 'DBC', 'MTUM', 'IWD', 'EFA', 'VNQ', 'EFV')


# # 19. Diversified GEM Dual Momemtum

# In[648]:


eq_weight('SPY', 'EFA', 'AGG')


# # 20. Vigilant Asset Allocation G12

# In[649]:


eq_weight('SPY', 'IWM', 'QQQ', 'VGK', 'EWJ', 'EEM', 'VNQ', 'DBC', 'GLD', 'TLT', 'LQD', 'HYG', 'IEF', 'BIL')


# # 21. Vigilant Asset Allocation G4

# In[650]:


eq_weight('SPY', 'EFA', 'EEM', 'AGG', 'LQD', 'IEF', 'BIL')


# # 22. Kipnis Defensive Adaptive Asset Allocation

# In[651]:


eq_weight('SPY', 'VGK', 'EWJ', 'EEM', 'VNQ', 'RWX', 'IEF', 'TLT', 'DBC', 'GLD', 'AGG')


# # 23. Generalized Protective Momentum 

# In[652]:


eq_weight('SPY', 'QQQ', 'IWM', 'VGK', 'EWJ', 'EEM', 'VNQ', 'DBC', 'GLD', 'HYG', 'LQD', 'BIL', 'IEF')


# # 24. The Trend is Our Friend

# In[ ]:





# # 25. Global Tactical Asset Allocation

# In[653]:


eq_weight('IWD', 'MTUM', 'IWN', 'DWAS', 'EFA', 'EEM', 'IEF', 'BWX', 'LQD', 'TLT', 'DBC', 'GLD', 'VNQ')


# # 26. Defensive Asset Allocation

# In[654]:


eq_weight('SPY', 'IWM', 'QQQ', 'VGK', 'EWJ', 'EEM', 'VNQ', 'BWX', 'DBC', 'TLT', 'HYG', 'GLD', 'LQD', 'SHY', 'IEF', 'AGG')


# # 27. Protective Asset Allocation

# In[655]:


eq_weight('IEF', 'IWM', 'QQQ', 'VNQ', 'SPY', 'VGK', 'EEM', 'EWJ', 'DBC', 'TLT', 'GLD', 'HYG', 'LQD')


# # 28. Adaptive Asset Allocation

# In[656]:


eq_weight('IEF', 'SPY', 'VNQ', 'RWX', 'DBC', 'EEM', 'VGK', 'EWJ', 'LQD', 'GLD')


# # 29. GEM Dual Momentum

# In[657]:


eq_weight('SPY', 'AGG', 'EFA')


# # 30. Quint Switching Filtered

# In[658]:


eq_weight('QQQ', 'EFA', 'EEM', 'SPY', 'TLT', 'IEF')


# # 31. Composite Dual Momentum

# In[659]:


eq_weight('SPY', 'EFA', 'HYG', 'VNQ', 'REM', 'GLD', 'TLT', 'LQD')


# In[ ]:




