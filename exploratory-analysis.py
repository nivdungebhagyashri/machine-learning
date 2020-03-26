#!/usr/bin/env python
# coding: utf-8

# # Problem Set 1
# 
# ### Before You Start
# 
# For this problem set, you should
# download flights.csv.bz2 and weather.csv.bz2 datasets from
# Canvas (files-data).   Rename the notebook to
# LASTNAME_FIRSTNAME-PS1.ipynb.
# 
# When done, please submit
# 1. the notebook itself
# 2. the rendered html or pdf of it.
# 
# Note: you do not have to use notebooks to solve this PS.  However, you have to submit
# * your code
# * your results
# * your explanations
# whatever means you use to solve this assignment.
# 
# It is all fine to discuss the problems and way how to solve these with
# your classmates and instructors.  However, the solutions must be your
# own.  Don't copy-paste each other solutions!

# ## About the Problem Set: 
# 
# This problem set is rather similar to ones used for R, dplyr, and
# flights data.  Just we use python and pandas.
# 
# Your task is to analyze the nycflights13 data (in the R package of the
#                                                same name).  The
#                                                necessary csv
# files are provided on canvas (in files/data).  An easy way to get the
# explanations is on the the [package page on R documentation](https://www.rdocumentation.org/packages/nycflights13/versions/1.0.0). 
# 
# In this problem set you will perform a basic exploratory analysis on
# an example dataset, bringing to bear all of your new skills in data
# manipulation and visualization. You will be required to submit well
# commented python code, documenting all code used in this problem set,
# along with a write up answering all questions below. Use figures as
# appropriate to support your answers, and when required by the problem.
# 
# Always comment your results, preferably in a separate markdown cell.
# 

# ## References
# 
# 1. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.mean.html
# 2. https://stackoverflow.com/questions/10202570/find-row-where-values-for-column-is-maximal-in-a-pandas-dataframe
# 3. https://thispointer.com/pandas-sort-rows-or-columns-in-dataframe-based-on-values-using-dataframe-sort_values/
# 4. https://stackoverflow.com/questions/17618981/how-to-sort-pandas-data-frame-using-values-from-several-columns
# 5. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
# 6. https://stackoverflow.com/questions/55145108/create-new-date-column-in-python-pandas
# 

# ## Preliminaries
# 
# You should also make sure the following libraries load correctly.
# Below are a few basic data description tasks already done for you. 

# In[5]:


#IPython is what you are using now to run the notebook
import IPython
print( "IPython version:      %6.6s (need at least 1.0)" % IPython.__version__)

# Numpy is a library for working with arrays and matrices
import numpy as np
print( "Numpy version:        %6.6s (need at least 1.7.1)" % np.__version__)

# SciPy implements many different numerical algorithms
import scipy as sp
print( "SciPy version:        %6.6s (need at least 0.12.0)" % sp.__version__)

# Pandas makes working with data tables easier
import pandas as pd
print( "Pandas version:       %6.6s (need at least 0.11.0)" % pd.__version__)

# Module for plotting
import matplotlib.pyplot as plt  
from pylab import *
print( "Mapltolib version:    %6.6s (need at least 1.2.1)" %
       matplotlib.__version__)
get_ipython().run_line_magic('matplotlib', 'inline')
# necessary for in-line graphics

# SciKit Learn implements several Machine Learning algorithms
import sklearn
print( "Scikit-Learn version: %6.6s (need at least 0.13.1)" %
       sklearn.__version__)
import os
# for certain system-related functions


# In[6]:


## Let's read the data and print some summary information
## adjust the path for your file system!
## you can find the path like this:
path = os.getcwd()
print(path)
flights_df= pd.read_csv('../data/flights.csv.bz2')


# In[7]:


## Extract some basic information about the data like number of rows,
## columns, column names, data types
print(flights_df.shape)
print(flights_df.columns)
print(flights_df.dtypes)


# In[4]:


## print the first and last few lines of the data
print("head\n", flights_df.head())
print("tail\n", flights_df.tail())
## Find the number of unique destinations in the data ('dest')
print("destinations:\n", flights_df.dest.unique())


# ## Some Tips
# 
# * This assignment involves extensive Data frame splitting and
#   aggregation. You should look into the details of the methods
#   groupby, transform, sum, count, mean etc 
# * Many of the tasks in the assignment can be done either through the
#   Pandas Data Frame or by converting the data frames to Series. Many
#   of the methods in the numpy are applicable to Series only. When
#   stuck, try to explore the type of object (Pandas Data Frame or Numpy
#   Series) you are dealing with. 

# ## Question 1
# 
# Let’s explore flights from NYC to LA. Use the flights dataset to answer the following questions.
# 
# ### (a)
# 
# How many flights were there from NYC airports to Los Angeles International Airport (LAX) in 2013?

# In[19]:


# Your code here
flights_df_nyc_to_lax = flights_df.loc[flights_df['dest'] == 'LAX']
len(flights_df_nyc_to_lax)


# ## Answer
# There are 16174 flights from NYC airports to LAX in 2013

# ### (b)
# 
# Which airline ('carrier') has the most flights from NYC to LAX? Which one has the least number of flights? Report the numbers respectively. 

# In[23]:


# Your code here
# Check number of flights for each airline
flights_df_nyc_to_lax['carrier'].value_counts()


# ## Answer
# UA has the maximum number of flights i.e 5823 from NYC to LAX where as B6 has the least number of flights i.e 1688. The numbers for each carrier are reported above.

# ### (c)
# 
# How many unique air planes fly from NYC to LAX?
# (Hint: use 'tailnum', essentially the license plate of airplane)

# In[24]:


# Your code here
flights_df_nyc_to_lax['tailnum'].nunique()


# ## Answer
# There are 991 unique flights from NYC to LAX
# 

# ### (d)
# 
# What is the average arrival delay for flights from NYC to LAX?

# In[25]:


# Your code here
flights_df_nyc_to_lax['arr_delay'].mean()


# ## Answer
# The average arrival delay for flights from NYC to LAX is 0.5471109447148383

# ### (e)
# 
# What proportion of flights to LAX come from each NYC airport?

# In[58]:


# Your code here
total_count = len(flights_df_nyc_to_lax)
jfk_count = len(flights_df_nyc_to_lax[flights_df_nyc_to_lax['origin']=='JFK'])
lga_count = len(flights_df_nyc_to_lax[flights_df_nyc_to_lax['origin']=='LGA'])
ewr_count = len(flights_df_nyc_to_lax[flights_df_nyc_to_lax['origin']=='EWR'])
print('Proportion Percentage of JFK Airport to LAX %.1f ' % ((jfk_count*100)/float(total_count)))
print('Proportion Percentage of LGA Airport to LAX %.1f ' % ((lga_count*100)/float(total_count)))
print('Proportion Percentage of EWR Airport to LAX %.1f ' % ((ewr_count*100)/float(total_count)))


# ## Question 2
# 
# Now let's explore the entire NYC flight dataset. Flights are often delayed. Consider the following questions exploring delay patterns.
# 
# ### (a)
# 
# Which date has the largest average departure delay? Which date has the largest average arrival delay?

# In[77]:


# Your code here
# Adding the Date column by concatenating yyyy-mm-dd
flights_df['date'] = flights_df['year'].astype(str) + "-" + flights_df['month'].astype(str) + "-" + flights_df['day'].astype(str)
# Creating a new dataframe with departure delay averages by date
avg_by_date = pd.DataFrame(flights_df.groupby('date').mean())

# Finding the date with the maximum average departure delay
print 'The date with largest average departure delay is'
print avg_by_date.sort_values(['dep_delay'], ascending = False)['dep_delay'].head(1)


# Finding the date with the maximum average arrival delay
print '\nThe date with largest average arrival delay is'
print avg_by_date.sort_values(['arr_delay'], ascending = False)['arr_delay'].head(1)


# ### (b)
# 
# What was the worst day and the best day to fly out of NYC in 2013
# if you dislike delayed flights?
# 
# Note: we ask the largest delay given there was a (positive) delay, we
# don't care about flights that were in time or early.

# In[113]:


# Your code here
# Highest departure delay of a flight in a day. 
dep_delay = flights_df[flights_df['dep_delay'] > 0]
dep_delay = dep_delay.set_index(['date'])
print "\nHighest delay in the departure of a flight was on:"
print dep_delay.sort_values(['dep_delay'], ascending = False)['dep_delay'].head(1)
print "\Smallers delay in the departure of a flight was on:"
print dep_delay.sort_values(['dep_delay'], ascending = True)['dep_delay'].head(1)


# ## Answer
# The worst day to fly out of NYC in 2013 is 2013-1-9 and best day to fly out of NYC is 2013-4-25

# ### (c)
# 
# On average which airline has the lowest departure delay for
#    their NYC flights in 2013 in this dataset? and which one has the
#    greatest departure delay?
# 
# Note: here we want to include both positive and negative delays (early departures)   

# In[85]:


# Your code here
flights_df.groupby('carrier')['dep_delay'].mean()


# ## Answer
# The airline F9 has the highest departure delay of 20.215543 and airline US has the smallest departure delay of 3.782418

# ### (d)
# 
# Are there any seasonal patterns in departure delays for flights from NYC?

# In[87]:


# Your code here
flights_df.head()
matplotlib.style.use('ggplot') 
plt.plot(flights_df.groupby('month')['dep_delay'].mean())
plt.xlabel('Months', size = 12)
plt.ylabel('Avg Departure delay in mins', size = 12)
plt.title('Avg Departure Delay in mins by Month')
plt.show()

# Exploring the seasonal patterns in total number of delayed by Month
plt.plot(dep_delay.groupby('month').count())
plt.xlabel('Months', size = 12)
plt.ylabel('Total Number of Delayed Flights', size = 12)
plt.title('Total Number of Delayed Flights by Month')
plt.show()


# ## Answer
# Yes, there seem to be some patterns in the flight departure delays. Mostly, the holiday season shows spike in the average flight departure delay time during the months of June, July and December. These months have the highest average delayed time. The second graph also shows the total number of flights delayed in a given month and again July and December comes out with most number of delayed flights in total. This clearly shows that the Summer and winter break are the periods where people take during these months of the year in terms of season.

# ### (e)
# 
# On average, how do departure delays vary over the course of a day?

# In[88]:


# Your code here
# Exploring data for departure delay trends over the course of a day
dep_delay_hour = pd.DataFrame(flights_df.groupby('hour')['dep_delay'].mean()) # Group by hour
dep_delay_hour.index.name = None

# Plotting Data
fig, ax = plt.subplots()
plt.bar(range(25), dep_delay_hour.dep_delay, 0.70)
plt.xlabel('Hour of the Day', size = 12)
plt.ylabel('Avg Departure Delay', size = 12)
plt.title('Avg Departure Delay over the course of a day')
plt.show()

# Calculating the number of flights by hour of the day
count_flights_hour = flights_df.groupby('hour').count()
count_flights_hour.rename(columns={'Unnamed: 0': 'count'}, inplace=True)
count_flights_hour.index.name = None


# ## Answer
# From the plot it is clear that the delays are more prominent during the night mainly between 10 PM and 4 AM. A possible reason could be low visibility condition during these hours or other factors like fog or bad weather conditions. The delay in flight departures go down significantly in other hours of the day. 
# 
# Also, another point to note is that the number of flights in these late hours are fewer than others. This can be a  possible reason why the average of the departure delay times is higher during 10 PM - 4 AM (fewer flights and most flights delayed: Example: Only 11 flights around 3 AM).
# 

# 
# 
# ## Question 3
# 
# Which flight departing NYC in 2013 flew the slowest?
# 
# Note: compute the speed as distance/time.

# In[109]:


# Your code here
flights_df['speed'] = flights_df.distance/(flights_df.air_time/60)
x = ['date','carrier','tailnum','flight','origin','dest','air_time','distance','speed']
flights_df.sort_values('speed',ascending = True)[x].head(1)


# ## Answer
# The flight 1860 flew the slowest of carrier US with tailnum N755US. The flight covered the distance of 96 miles in 75 mins with an average speed of 76.8 miles per hour.
# 

# ## Question 4
# 
# Which flights (i.e. carrier + flight + dest) happen every day? Where do they fly to?

# In[100]:


# Your code here
flights_df['flight_combo'] = flights_df['carrier'].astype(str) + ' ' + flights_df['flight'].astype(str) + ' ' + flights_df['dest'].astype(str)
flights_df.head()

# Just checking the dates that are present in the dataset and getting a count
dates = pd.DataFrame(flights_df.date.unique())
dates.rename(columns={0:'date'}, inplace = True)
print "\nFor a flight to fly every day, it needs to fly these number of days: ", dates.date.count()

# Grouping by flight and date to see which flights fly on which days of the year
flights_rep = flights_df.groupby(['flight_combo','date']).count()
flights_rep.reset_index(level=0, inplace=True) # getting rid of the flight_combo index from the dataframe
flights_rep.reset_index(level=0, inplace=True) # getting rid of the date index from the dataframe
flights_rep.rename(columns={'Unnamed: 0':'count'}, inplace = True)

# Counting number of days a given flight combo flies
flights_rep = flights_rep.groupby('flight_combo').count().sort_values('count', ascending = False) 
flights_rep.reset_index(level=0, inplace=True)

# Getting only flights that fly on all days (365 unique days of the current dataset)
flights_all_days = flights_rep[flights_rep['count'] == 365]['flight_combo']
print "\nThe flights (i.e. carrier + flight + dest) happen every day are: \n",flights_all_days

# Getting the destinations they fly to
destinations = []
for f in flights_all_days.astype(str):
    destinations.append(f[len(f)-3:])
destinations = set(destinations)
print "\nThe flights that fly every day fly to the following destinations: \n\n", destinations


# ## Answer
# The following flights fly every day of the year 2013 from NYC:
#       1. UA 15 HNL
#       2. B6 371 FLL
#       3. AA 181 LAX
#       4. B6 219 CLT
#       5. AA 119 LAX
#       6. B6 703 SJU
#       7. DL 2391 TPA
#       8. AA 1357 SJU
#       9. EV 5712 IAD
#       10. VX 251 LAS
#       11. AA 1611 MIA
#       12. VX 413 LAX
#       13. DL 2159 MCO
#       14. B6 431 SRQ
#       15. VX 407 LAX
#       16. AA 59 SFO
#       17. B6 1783 MCO
#       18. B6 359 BUR
#       
# The flights that fly every day fly to the following destinations:
#  
#       1. 'MCO' -- Orlando International Airport (FL)
#       2. 'TPA' -- Tampa International Airport (FL)
#       3. 'MIA' -- Miami International Airport (FL)
#       4. 'IAD' -- Washington Dulles International Airport (VI)
#       5. 'HNL' -- Honolulu International Airport
#       6. 'SJU' -- San Juan Airport Hotel (Puerto Rico)
#       7. 'SFO' -- San Francisco International Airport (CA)
#       8. 'SRQ' -- Sarasota–Bradenton International Airport (FL)
#       9. 'LAX'-- Los Angeles International Airport (CA)
#       10. 'FLL' -- Fort Lauderdale–Hollywood International Airport (FL)
#       11. 'CLT' -- Charlotte Douglas International Airport (NC)
#       12. 'BUR' -- Bob Hope Airport (CA)
#       13. 'LAS' -- McCarran International Airport (CA)
#      
#  
# These flights are between NY and the following places: California, Florida, Virginia, North Carolina and Puerto Rico

# ## Question 5
# 
# Develop one research question you can address using the nycflights2013
# dataset. Provide two visualizations to support your exploration of
# this question. Discuss what you find. 
# 
# Note: we'll using matplotlib for plotting in this course, but you can use something else too.

# In[114]:


# Your code here
'''Research Question: 1. In 2013, which airlines and airports showcases best positive experience for NY flyers? 
                      2. How can users make smarter decisions for traveling to specific destinations? '''

### Exploring first part of the research question -- what are the best destinations to fly from NYC

# Finding the destination statistics 
dest_avgs = flights_df.groupby('dest')['dep_delay','arr_delay','speed_in_mph'].mean()
dest_avgs.reset_index(level=0, inplace=True)

# Cleaning up data further
total_flights = flights_df.groupby('dest').count()
total_flights.reset_index(level=0, inplace=True)
total_flights.rename(columns = {'Unnamed: 0':'count'}, inplace = True)
dest_avgs['total_flights_count'] = total_flights['count']
dest_avgs = dest_avgs[np.isfinite(dest_avgs['dep_delay'])]
dest_avgs = dest_avgs[np.isfinite(dest_avgs['arr_delay'])]
dest_avgs = dest_avgs[np.isfinite(dest_avgs['speed_in_mph'])]

rcParams['figure.figsize'] = 20, 20

# Preparing for plotting
x = list(dest_avgs['dep_delay'])
y = list(dest_avgs['arr_delay'])
# The color of the bubbles show the speed of the flights
color = list(dest_avgs['speed_in_mph']) 
# The size of the bubbles show the number of flights to that destination
area = list(dest_avgs['total_flights_count']) 
s = list(dest_avgs['dest'])

i = 0
while(i<len(dest_avgs)):
    text(x[i],y[i],s[i],size=12, verticalalignment='center', horizontalalignment='center', color='black', alpha = 0.7)
    i = i+1

sct = scatter(x, y, c=color, s=area, linewidths=2, edgecolor='w')
sct.set_alpha(0.50)

axis([-15,40,-25,43])
xlabel('Avg departure delays in mins')
ylabel('Avg arrival delay in mins')
title('Destinations for NY flyers (Size of the bubble denotes the number of flights flying to a given destination)')

show()

print "The top 5 destinations to travel to:\n\n", dest_avgs.sort_values(['arr_delay','dep_delay']).head(5)
print "\n\nThe worst 5 destinations to travel to:\n\n", dest_avgs.sort_values(['arr_delay','dep_delay']).tail(5)


# In[102]:


### Exploring the second part of the research question, what are the best airlines to fly with 

# Finding the destination statistics 
carrier_avgs = flights_df.groupby('carrier')['dep_delay','arr_delay','speed_in_mph'].mean()
carrier_avgs.reset_index(level=0, inplace=True)

# Cleaning up data further
total_flights_ca = flights_df.groupby('carrier').count()
total_flights_ca.reset_index(level=0, inplace=True)
total_flights_ca.rename(columns = {'Unnamed: 0':'count'}, inplace = True)
carrier_avgs['total_flights_count'] = total_flights_ca['count']
carrier_avgs = carrier_avgs[np.isfinite(carrier_avgs['dep_delay'])]
carrier_avgs = carrier_avgs[np.isfinite(carrier_avgs['arr_delay'])]
carrier_avgs = carrier_avgs[np.isfinite(carrier_avgs['speed_in_mph'])]


# Preparing for plotting
x2 = list(carrier_avgs['dep_delay']) # X axis shows the departure delay in mins
y2 = list(carrier_avgs['arr_delay']) # Y axis shows the arrival delay in mins
color2 = list(carrier_avgs['speed_in_mph']) # The color of the bubbles show the speed of the flights
area2 = list(carrier_avgs['total_flights_count']) # The size of the bubbles show the number of flights to that destination
s2 = list(carrier_avgs['carrier'])

i = 0
while(i<len(carrier_avgs)):
    text(x2[i],y2[i],s2[i],size=14, verticalalignment='center', horizontalalignment='center', color='black', alpha = 0.7)
    i = i+1

sct2 = scatter(x2, y2, c=color2, s=area2, linewidths=2, edgecolor='w')
sct2.set_alpha(0.4)
rcParams['figure.figsize'] = 20, 20

axis([0,25,-15,25])
xlabel('Avg departure delays in mins')
ylabel('Avg arrival delay in mins')
title('Carriers operating flights from NY (Size of the bubble denotes the number of flights operated by a carrier)')

show()

print "The top 5 carriers to travel with:\n\n", carrier_avgs.sort_values(['dep_delay','arr_delay']).head(5)
print "\n\nThe worst 5 carriers to travel with:\n\n", carrier_avgs.sort_values(['dep_delay','arr_delay']).tail(5)


# ## Question 6
# 
# What weather conditions are associated with flight delays leaving NYC?  Use graphics to explore.
# 
# Note: you need to use 'weather.csv' dataset

# In[115]:


# Your code here
weather_df = pd.read_csv('../data/weather.csv.bz2') # Importing the weather dataset 
# Aggregating data 
weather_df = pd.DataFrame(weather_df.groupby(['year','month','day','origin']).mean())
# Getting rid of the grouped indices
weather_df.reset_index(level = 0, inplace = True)
weather_df.reset_index(level = 0, inplace = True)
weather_df.reset_index(level = 0, inplace = True)
weather_df.reset_index(level = 0, inplace = True)

# retaining only useful columns
weather_df =  pd.DataFrame(weather_df[['origin','year','month','day','temp','dewp','humid','wind_dir',
                                       'wind_speed','wind_gust','precip','pressure','visib']]) 
weather_df.head()

# Aggregating data and eliminating grouped indices for flights data to make it uniform with weather data
flights_agg = flights_df.groupby(['year','month','day','origin']).mean()
flights_agg.reset_index(level = 0, inplace = True)
flights_agg.reset_index(level = 0, inplace = True)
flights_agg.reset_index(level = 0, inplace = True)
flights_agg.reset_index(level = 0, inplace = True)

flights_agg = flights_agg[['origin','year','month','day','dep_delay','arr_delay','speed_in_mph']]
flights_agg.head()

# Merging datasets
flights_weather = pd.merge(weather_df,flights_agg, on = ['year','month','day','origin'], how = 'inner')

matplotlib.style.use('ggplot')

rcParams['figure.figsize'] = 20, 20
fig = plt.figure()
ax1 = fig.add_subplot(331)
ax1.scatter(flights_weather['temp'], flights_weather['dep_delay'], c = 'darkred')
xlabel('Avg Temp in F')
ylabel('Avg departure delay in mins')
title('Temp Vs. Departure Delay')

ax2 = fig.add_subplot(332)
ax2.scatter(flights_weather['visib'], flights_weather['dep_delay'], c = 'grey')
xlabel('Average Visibility in miles')
ylabel('Avg departure delay in mins')
title('Visibility Vs. Departure Delay')

ax3 = fig.add_subplot(333)
ax3.scatter(flights_weather['dewp'],flights_weather['dep_delay'], c = 'darkblue')
xlabel('dewpoint in F')
ylabel('Avg departure delay in mins')
title('Dewpoint Vs. Departure Delay')

ax4 = fig.add_subplot(334)
ax4.scatter(flights_weather['precip'], flights_weather['dep_delay'], c = '#4d4dff')
xlabel('Avg precipitation in inches')
ylabel('Avg departure delay in mins')
title('Precipitation Vs. Departure Delay')

ax5 = fig.add_subplot(335)
ax5.scatter(flights_weather['humid'], flights_weather['dep_delay'], c = '#004c99')
xlabel('Relative humidity')
ylabel('Avg departure delay in mins')
title('Relative Humidity Vs. Depature Delay')

ax6 = fig.add_subplot(336)
ax6.scatter(flights_weather['pressure'], flights_weather['dep_delay'], c = '#ff661a')
xlabel('Sea level pressure in millibars')
ylabel('Avg departure delay in mins')
title('Pressure Vs. Depature Delay')

ax7 = fig.add_subplot(337)
ax7.scatter(flights_weather['wind_speed'], flights_weather['dep_delay'], c = 'darkred')
xlabel('Wind speed in mph')
ylabel('Avg departure delay in mins')
title('Wind Speed Vs. Depature Delay')

ax8 = fig.add_subplot(338)
ax8.scatter(flights_weather['wind_gust'], flights_weather['dep_delay'], c = '#333300')
xlabel('Wind gust in mph')
ylabel('Avg departure delay in mins')
title('Wind Gust Vs. Depature Delay')

ax9 = fig.add_subplot(339)
ax9.scatter(flights_weather['wind_dir'], flights_weather['dep_delay'])
xlabel('Wind direction in degrees')
ylabel('Avg departure delay in mins')
title('Wind Direction Vs. Depature Delay')

# Exploring Monthly trends and relationships

flights_weather_month = flights_weather.groupby('month').mean()
flights_weather_month.reset_index(level=0, inplace = True)
flights_weather_month['precip'] = flights_weather_month['precip'] * 1000000

x = list(flights_weather_month['temp'])
y = list(flights_weather_month['dep_delay'])
color = list(flights_weather_month['visib'])
# The size of the bubbles show the number of flights to that destination
area = list(flights_weather_month['precip'])
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

matplotlib.style.use('ggplot')

rcParams['figure.figsize'] = 13, 7
fig2 = plt.figure()

ax1 = fig2.add_subplot(111)
ax1.scatter(x, y, c=color, s=area, linewidths=2, edgecolor='w',alpha = 0.5, label = 'Trends')
i = 0
while(i<len(flights_weather_month)):
    text(x[i],y[i],months[i],size=12, verticalalignment='center', horizontalalignment='center', color='white')
    i = i+1
xlabel('Monthly Avg Temperature in F')
ylabel('Avg departure delay in mins')
title('Avg Temperature Vs. Departure Delay Monthly Trends (Area of the bubble denotes precipitation of the order 10^-6 inches)', size = 12)
show()

print '\n -------------------------------------- \n' 


# ## Answer
# Visibility, precipitation and temperature seem to be most interesting so we plot a bubble chart showing all these factors on a monthly scale. From the bubble chart, its clear that the months of December, June and July had the highest departure delays. The month of June had most precipitation (the area of bubble denotes the precipitation levels), July had the highest temperature and December had low temperatures and good precipitation.
# 
# 

# # Grading
# 
# * Q1: 1pt each question (5 in total)
# * Q2: a) 2pt, b) 3pt, c) 2pt, d) 2pt, e) 1pt
# * Q3: 5pt
# * Q4: 5pt
# * Q5: 15pt
# * Q6: 10pt

# In[ ]:




