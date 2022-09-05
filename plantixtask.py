#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[49]:


import pandas as pd
import matplotlib.pyplot as plt


# In[50]:


lg=pd.read_csv('C:\\Users\\dell\\Downloads\\login_logs.csv')


# In[51]:


lg


# In[52]:


soi=pd.read_csv('C:\\Users\\dell\\Downloads\\sales_orders_items.csv')


# In[53]:


soi


# In[54]:


so=pd.read_csv('C:\\Users\\dell\\Downloads\\sales_orders.csv')


# In[55]:


so


# In[56]:


lg.info()


# In[57]:


lg.login_time.nunique()


# In[58]:


#print(lg.login_time.mean())


# In[59]:


so.order_id.nunique()


# In[85]:


soi.fk_product_id.nunique()


# In[60]:


# Assigning a log column to each logintime
lg['log'] = lg['login_time']
lg['user']= lg['user_id']
# Calculating total number of posts per week for each user
total_logs = lg.groupby(['user', 'log']).size().reset_index(name ='Total_logs')

# Estimating average frequency of making logs for each user
freq_login_per_logs = total_logs.groupby('log')['Total_logs'].mean().reset_index(name ='Avg_login_per_logs')


# In[61]:


freq_login_per_logs 


# In[62]:


# Assigning sales column to each order
soi['sales'] = soi['ordered_quantity']
soi['order']= soi['order_quantity_accepted']
# Calculating total number of posts per week for each user
total_sales = soi.groupby(['sales','order']).size().reset_index(name ='Total_sales')

# Estimating average frequency of making logs for each user
freq_sales_per_person = total_sales.groupby('sales')['Total_sales'].mean().reset_index(name ='Avg_sales_per_person')


# In[63]:


freq_sales_per_person


# In[66]:


x1=soi['order_quantity_accepted']
plt.plot(x1)

plt.show()


# In[84]:


x1=soi['order_item_id']
 
plt.plot(x1)

plt.show()


# In[81]:



x = so['order_id'].count()


print(x)


# In[103]:


x=soi['fk_product_id']
y=soi['ordered_quantity']
plt.bar(x,y)
plt.show()


# In[109]:


x=soi['ordered_quantity']
y=soi['order_quantity_accepted']


plt.bar(x,y)
plt.show()


# In[111]:


x=soi['ordered_quantity']


plt.plot(x)
plt.show()


# In[ ]:




