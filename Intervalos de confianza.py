#!/usr/bin/env python
# coding: utf-8

# In[62]:


#Tarea 7 PyE, Estadística Inferencial
#Aguilar Cárcamo Marco Antonio


# In[27]:


data = pd.read_csv("file:///C:/Users/DELL/Downloads/2013_ACCIDENTS_GU_BCN_2013.csv")


# In[26]:


data['Date'] = '2013-'+data['Mes de any'].apply(lambda x : str(x)) + '-' +  data['Dia de mes'].apply(lambda x : str(x))
data['Date'] = pd.to_datetime(data['Date'])
accidents = data.groupby(['Date']).size()
print("Mean:", accidents.mean())


# In[39]:


import numpy as np
# population
df = accidents.to_frame()
N_test = 10000
elements = 200
# mean array of samples
means = [0] * N_test
# sample generation
for i in range (N_test):
    rows = np.random. choice(df.index. values , elements)
    sampled_df = df.loc[ rows]
    means[i] = sampled_df. mean()


# In[41]:


import math
rows = np.random. choice(df.index. values , 200)
sampled_df = df.loc[ rows]
est_sigma_mean = sampled_df.std()/ math.sqrt(200)
print("Direct estimation of SE from one sample of 200 elements:" , est_sigma_mean[0]) 
print ("Estimation of the SE by simulating 10000 samples of 200 elements:", np.array(means).std())


# In[43]:


def meanBootstrap(X, numberb):
    x = [0]* numberb
    for i in range (numberb):
        sample = [X[j]
            for j
            in np.random.randint( len(X), size=len(X))
        ]
        x[i] = np. mean(sample)
    return x
m = meanBootstrap( accidents , 10000)
print ("Mean estimate:", np.mean(m))


# In[44]:


m = accidents. mean()
se = accidents.std()/ math.sqrt(len(accidents))
ci = [m - se*1.96, m + se *1.96]
print ("Confidence interval:", ci)


# In[50]:


data = pd. read_csv("file:///C:/Users/DELL/Downloads/2010_ACCIDENTS_GU_BCN_2010.csv",
encoding='latin -1')
# Create a new column which is the date
data['Date'] = '2010-'+data['Dia de mes']. apply ( lambda x: str(x)) + '-' + data['Mes de any'].apply ( lambda x: str(x))
data2 = data['Date']
counts2010 = data['Date'].value_counts()
print ('2010: Mean', counts2010. mean())

data = pd. read_csv("file:///C:/Users/DELL/Downloads/2013_ACCIDENTS_GU_BCN_2013.csv", encoding='latin -1')
# Create a new column which is the date
data['Date'] = '2013-'+data['Dia de mes']. apply ( lambda x: str(x)) + '-' + data['Mes de any']. apply ( lambda x: str(x))
data2 = data['Date']
counts2013 = data['Date'].value_counts()
print ('2013: Mean', counts2013. mean())


# In[51]:


n = len(counts2013)
mean = counts2013. mean()
s = counts2013.std()
ci = [mean - s*1.96/np.sqrt(n), mean + s*1.96/np.sqrt (n)]
print ('2010 accident rate estimate:', counts2010. mean())
print ('2013 accident rate estimate:', counts2013. mean())
print ('CI for 2013:',ci)


# In[53]:


m = len(counts2010)
n = len(counts2013)
p = (counts2013. mean() - counts2010. mean())
print ('m:', m, 'n:', n)
print ('mean difference: ', p)


# In[58]:


# pooling distributions
x = counts2010
y = counts2013
pool = np. concatenate([x, y])
np.random. shuffle( pool)
#sample generation
import random
N = 10000 # number of samples
diff = np.arange (N)
for i in np.arange (N):
   p1 = [random. choice(pool) for _ in np.arange (n)]
   p2 = [random. choice(pool) for _ in np.arange (n)]
   diff[i] = (np.mean(p1) - np.mean(p2))


# In[60]:


# counting differences larger than the observed one
diff2 = np.array(diff)
w1 = np.where(diff2 > p)[0]
print ('p-value ( Simulation)=', len(w1)/ float (N),
'(', len(w1)/ float (N)*100 ,'%)', 'Difference =', p)
if ( len(w1)/ float (N)) < 0.05:
    print ('The effect is likely')
else :
    print ('The effect is not likely')

