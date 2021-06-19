#!/usr/bin/env python
# coding: utf-8

# # Capstone Project - The Battle of the Neighborhoods (Week 1)
# ### Applied Data Science Capstone by IBM/Coursera

# ## Table of contents
# * [Introduction: Business Problem](#introduction)
# * [Data](#data)

# 
# 
# ## Introduction: Business Problem <a name="introduction"></a>

# Recently, there has been a steadily increasing trend that HongKongers love doing outdoor activities.
# 
# In this project, we will find an optimal location of opening an outdoor activities center, by filtering out nature neighborhoods amoung 18 districts in Hong Kong. Because the more nature elements in neighborhoods will make outdoor activities more accessible and attractive.

# ## Data <a name="data"></a>

# Official District Councils website (https://www.districtcouncils.gov.hk/index.html) contains all the areas located in 18 districts in Hong Kong, with the following columns:
# - Area
# - Districts
# 
# Using Open Street Map (OSM) - Nominatim to retrieve a specific location's latitude & longitude, with the following columns:
# - Districts (neighborhood)
# - latitude
# - longitude
# 
# Using FourSquare to retrieve a specific location's nearby venues, with the following columns:
# - Neighborhood
# - Venue's latitude
# - Venue's longitude
# - Venue's category

# In[ ]:




