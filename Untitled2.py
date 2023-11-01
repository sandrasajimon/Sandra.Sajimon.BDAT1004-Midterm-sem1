#!/usr/bin/env python
# coding: utf-8

# In[1]:


WITH WeatherRanked AS(
    SELECT 
      id,
      recordDate,
      temperature,
      LAG(temperature) OVER (ORDERED BY record Date)
AS prevTemperature
    FROM Weather
)
SELECT id
FROM WeatherRanked
WHERE temperature > prevTemperature:
    


# In[ ]:




