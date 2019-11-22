#!/usr/bin/env python
# coding: utf-8

# # Imports & Setup

# In[21]:


import pandas as pd
import numpy as np


# **Creating Dataframe**

# In[2]:


df = pd.read_csv('Data/Tweets.csv')


# **How our data looks like**

# In[3]:


df.head(3)


# In[4]:


df.info()


# **Put data inc correct types**

# In[7]:


print('airline_sentiment', type(df.airline_sentiment.loc[0]))
print('negativereason', type(df.negativereason.loc[0]))
print('airline', type(df.airline.loc[0]))
print('airline_sentiment_gold', type(df.airline_sentiment_gold.loc[0]))
print('name', type(df.name.loc[0]))
print('negativereason_gold', type(df.negativereason_gold.loc[0]))
print('text', type(df.text.loc[0]))
print('tweet_coord', type(df.tweet_coord.loc[0]))
print('tweet_created', type(df.tweet_created.loc[0]))
print('tweet_location', type(df.tweet_location.loc[0]))
print('user_timezone', type(df.user_timezone.loc[0]))


# In[8]:


df[['airline_sentiment','text','airline']]


# In[17]:


import matplotlib.pyplot as plt
plt.plot(df.airline_sentiment.)


# In[34]:


plt.bar(df.airline_sentiment.unique(), df.airline_sentiment.value_counts())


# In[ ]:




