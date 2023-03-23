#!/usr/bin/env python
# coding: utf-8

# # Part I - Suicide Rate Analysis
# ## by Philip Obiorah
# 

# ### Introduction
# According to World Health Organization (WHO), every year nearly 800 000 people die due  to  suicide.  Suicides  are  preventable.  There  are  several  measures  that  can  be taken at population, subpopulation, and individual levels to prevent suicide and suicide attempts.
# 
# 
# In this project, we shall try to understand which age groups are vulnerable to suicide, we will look at the suicide rates of countries involved in the surveys from 1985 to 2016 provided in the dataset named WHO_Suicide_Data.csv.
# 
# Note: The dataset is not clean, and data might not be absolutely correct. Whatever conclusions drawn from this exercise, should be interpreted in that light.

# ### Gathering

# In[508]:


#Import the requied libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[509]:


#Load the dataset (WHO_Suicide_Data.csv)
suicide_data = pd.read_csv("WHO_Suicide_Data.csv")
suicide_data.head()


# ### Accessing Data
# WHO Suicide Data

# In[510]:


suicide_data


# In[511]:


# View the datatypes
suicide_data.dtypes


# *WHO Suicide Data * :
# Dataset has 27840 rows and 9 columns
# ##### suicide_data columns :
# - country: Country which has record of suicides
# - year : Year in which suicides were  recorded	
# - sex	: Gender of the individuals who committed suicide
# - age	: Age range of the the individuals who committed suicide
# - suicides_no	: Number of suicide committed with a certain year
# - population : Population of the age group within the country 	
# - gdp_for_year ($) Gross Domestic Product of the country

# In[512]:


# Random selection of 10 samples for visual accessment  
suicide_data.sample(10)


# In[513]:


# Lets check for Quality and Tidyness
suicide_data.info()


# In[514]:


# Let us check for null values
suicide_data.isnull().sum()


# In[515]:


#Let us check for duplicate rows
suicide_data.duplicated().sum()


# In[516]:


# View duplicate rows
suicide_data[suicide_data.duplicated()]


# In[517]:


#Lets check the values in the sex column
suicide_data["sex"].unique()


# In[518]:


#Descriptive stats for numeric values
suicide_data.describe()


# #### (a) Issues/Problems Identified in the dataset
# - Missing data in `suicides_no` 
# - Two unnamed and empty columns
# - Space in column name for gdp_for_year 
# - Incorrect datatype for ` gdp_for_year ($)
# - Incorrect datatye for `suicides_no`
# - String objects in gdp_for_year has commas`
# - There are 20 duplicate rows
# - 'suicides_no' column contains other non-numeric values  present in the column
# 

# ### Data Cleaning

# In[519]:


#Let us make a copy of the orignal dataset.
suicide_data_clean = suicide_data.copy()


# #### Two unnamed and empty columns

# ##### Define
# - Drop empty columns `Unnamed: 7` and `Unnamed: 8`

# ##### Code

# In[520]:


# Drop empty columns Unnamed: 7 and Unnamed: 8
suicide_data_clean = suicide_data_clean.drop(['Unnamed: 7','Unnamed: 8'], axis=1)


# ##### Test

# In[521]:


# Test to confirm  empty columns Unnamed: 7 and Unnamed: 8 are dropped
suicide_data_clean.head()


# #### Missing data in suicides_no

# ##### Define
# - Remove rows with missing data
# 

# ##### Code

# In[522]:


# Let us drop rows with missing data
suicide_data_clean= suicide_data_clean.dropna()


# ##### Test

# In[523]:


# Confirm that `suicides_no` is now int
suicide_data_clean['suicides_no'].dtype


# In[524]:


# Test to confirm that there are no null values or missing values
suicide_data_clean.isnull().sum()


# In[525]:


# Test to confirm that other rows remained after removing rows with missing data.
suicide_data_clean.info()


# In[526]:


suicide_data_clean.columns


# #### Space in column name for gdp_for_year ($)

# ##### Define
# - Rename column `gdp_for_year ($)` to `gdp_for_year`
# 

# ##### Code

# In[527]:


#Rename column `gdp_for_year ($)` using index number
suicide_data_clean = suicide_data_clean.rename(columns={' gdp_for_year ($) ': 'gdp_for_year'})
suicide_data_clean['gdp_for_year']


# ##### Test

# In[528]:


#Test renaming of column `gdp_for_year ($)` to `gdp_for_year`
suicide_data_clean.columns.values


# In[529]:


#Test renaming of column `gdp_for_year ($)` to `gdp_for_year`
suicide_data_clean


# #### String objects in gdp_for_year has commas`

# ##### Define
# - Replace the commas in `gdp_for_year` column with `''`(empty strings)

# ##### Code
# 

# In[530]:


#Replace the commas in gdp_for_year column with ''(empty strings)
suicide_data_clean['gdp_for_year'] = suicide_data_clean['gdp_for_year'].str.replace(',', '')


# ##### Test

# In[531]:


# Test replacement the commas in gdp_for_year column with ''(empty strings)
suicide_data_clean['gdp_for_year']


# #### Incorrect datatype for ` gdp_for_year 
# #### Incorrect datatye for `suicides_no`

# ##### Define
# - Change datatype for gdp_for_year to integer
# - Change datatype for `suicides_no` to integer

# ##### Code

# In[532]:


# Change datatype for gdp_for_year to integer
suicide_data_clean['gdp_for_year'] = suicide_data_clean['gdp_for_year'].astype(int)


# ##### Test

# In[533]:


# Test change  of datatype for gdp_for_year to integer
suicide_data_clean['gdp_for_year'].dtype


# #### `suicides_no` column has other non-numeric values  present in the column
# 

# ##### Define
# - Replace any non-numeric values with NaN using the pd.to_numeric method
# - Drop any rows with missing values

# ##### Code

# In[534]:


#Replace any non-numeric values with NaN using the pd.to_numeric method
suicide_data_clean['suicides_no'] = pd.to_numeric(suicide_data_clean['suicides_no'], errors='coerce')


# In[535]:


#Drop any rows with missing values
suicide_data_clean.dropna(subset=['suicides_no'], inplace=True)


# ##### Test

# In[536]:


# Confirm that their are no Null or NaN 
suicide_data_clean['suicides_no'].isna().sum()


# In[ ]:





# #### Incorrect datatye for suicides_no

# ##### Define
# - Convert the 'suicides_no' column to integer

# ##### Code 

# In[537]:


# Convert the 'suicides_no' column to integer
suicide_data_clean['suicides_no'] = suicide_data_clean['suicides_no'].astype(int)


# ##### Test

# #### There are 20 duplicate rows

# ##### Define
# - Remove duplicate rows 

# ##### Code
# 

# In[538]:


#Remove duplicate rows 
suicide_data_clean = suicide_data_clean.drop_duplicates(keep="first")


# ##### Test

# In[539]:


# Confirm that there are no more duplicate rows
suicide_data_clean.duplicated().sum()


# In[540]:


# View the the shape of the dataset
suicide_data_clean.shape


# In[541]:


# view the numerical dataset 
suicide_data_clean.describe()


# ### Data Storage

# After the data cleaning process it is appropriate that we store our clean datasdet into a new csv file

# In[542]:


suicide_data_clean.to_csv('suicide_data_clean.csv', index=False)


# ### Data Analysis

# We shall attempt to implement the following in our analysis
# - (b) Add  a  new  column “suicides/100k”  and  generate  its  data  suicides/100k population  of  a  country  is  the  population  of  a  specific  age  group  and  gender within that country divided by 100000, and the number of suicides divided by that number  Example: Its “suicides/100k” value is 21/(312900/100000) = 6.7114
# - (c) Add a new column “generation” and fill up its data according to below criteria 
# | Value | Criteria | 
# | --- | --- |
# | Lost Generation  | born between 1883 -1900 | 
# | G.I. Generation  | born between 1901 -1927 | 
# | Silent    | born between 1928 -1945 | 
# | Boomers | born between 1946 –1964 | 
# | Generation X  | born between 1965 -1980 | 
# | Millennials   | born between 1981 -1996 | 
# | Generation Z   | born between 1997–2012 | 
# | Generation A    | born between 2013–2025 | 
# 
# 
# 
# 
# 
# - d)Add a new  column  “gdp_per_capita” and  fill  its  data.  GDP  per  Capita  of a country is GDP divided by population of that country
# - e)Rank countries by total suicides
# - f)Find the correlations between suicides, GDP per capita and population. What are your conclusions?
# - g)Use appropriate visual notation to visualise total suicides over years. Describe your findings
# - h)Compare suicides by gender over years and state your conclusions
# - i)Calculate  and  Visualise  suicides  on  generation  and  on  age  group.  Describe your findings.
# - Code modularity –use of sensible variable names, code structure, comments 

# We shall load the `suicide_data_clean.csv` into `suicide_master_df` dataframe.

# In[543]:


#load the clean suicide dataset
suicide_master_df = pd.read_csv("suicide_data_clean.csv")
suicide_master_df.sample(20)


# #### (b) Add a new column “suicides/100k” and generate its data suicides/100k population of a country is the population of a specific age group and gender within that country divided by 100000, and the number of suicides divided by that number 
# #Example: Its “suicides/100k” value is 21/(312900/100000) = 6.7114

# In[544]:


#(b) Add a new column “suicides/100k” and generate its data suicides/100k population of a country is the population of a specific age group and gender within that country divided by 100000, and the number of suicides divided by that number 
#Example: Its “suicides/100k” value is 21/(312900/100000) = 6.7114
suicide_master_df['suicides/100k'] = suicide_master_df['suicides_no']/(suicide_master_df['population']/100000)


# In[545]:


#Test that suicide_master_df now has the suicides/100k
suicide_master_df


# In[546]:


age = suicide_master_df["age"][0]


# In[547]:


age.split('-')[0].split(' ')[0]


# In[548]:


suicide_master_df['year'].iloc[0]


# #### c) Add a new column “generation” and fill up its data according to below criteria

# In[549]:


# define a function to extract birth year from age              int(age[:-7])
def extract_birth_year(age): 
    if '-' in age:
    
        age_range = age.split('-')[0].split(' ')[0]
        birth_year = suicide_master_df['year'].iloc[0] - int(age_range)
        
    else:
        age_range = int(age[:-7])
        birth_year = suicide_master_df['year'].iloc[0] - age_range
    
    return birth_year


# In[ ]:





# In[550]:


# apply the function to age column and create a new column for birth year
suicide_master_df['birth_year'] = suicide_master_df['age'].apply(extract_birth_year)


# In[551]:


suicide_master_df


# In[552]:


def assign_generation(birth_year):
    if 1883 <= birth_year <= 1900:
        return "Lost Generation"
    elif 1901 <= birth_year <= 1927:
        return "G.I. Generation"
    elif 1928 <= birth_year <= 1945:
        return "Silent"
    elif 1946 <= birth_year <= 1964:
        return "Boomers"
    elif 1965 <= birth_year <= 1980:
        return "Generation X"
    elif 1981 <= birth_year <= 1996:
        return "Millennials"
    elif 1997 <= birth_year <= 2012:
        return "Generation Z"
    elif 2013 <= birth_year <= 2025:
        return "Generation A"
    else:
        return "Unknown"


# In[553]:


# Apply the function to the birth year column to create a new "generation" column
suicide_master_df["generation"] = suicide_master_df["birth_year"].apply(assign_generation)


# In[554]:


# Drop the "birth_year" column as it's no longer needed
suicide_master_df.drop("birth_year", axis=1, inplace=True)


# In[555]:


# Test and confirm that the current dataframe has the generation column
suicide_master_df.sample(30)


# #### d)Add a new column “gdp_per_capita” and fill its data. GDP per Capita of a country is GDP divided by population of that country

# In[556]:


suicide_master_df['gdp_per_capita'] = suicide_master_df['gdp_for_year']/suicide_master_df['population']


# In[557]:


suicide_master_df


# #### e)Rank countries by total suicides

# In[558]:


# group the dataframe by country and sum the suicides_no column
country_suicides = suicide_master_df.groupby('country')['suicides_no'].sum()


# In[559]:


# rank the countries based on their total suicides
ranked_countries = country_suicides.rank(ascending=True)


# In[560]:


# print ranked countries
print(ranked_countries)


# In[561]:


ranked_countries.head(10).index


# In[562]:


# Top ranked countries by suicide
ranked_countries.head(10).plot(kind="bar", xlabel='country' , ylabel="Rank of Suicide")


# ####  f)Find the correlations between suicides, GDP per capita and population. What are your conclusions?

# In[563]:


correlations = suicide_master_df[['suicides_no', 'gdp_per_capita', 'population']].corr()
print(correlations)


# In[564]:


sns.heatmap(correlations, annot=True, cmap='coolwarm')


# The value -0.003 indicates a weak negative correlation between the No of sucides and GDP per capita. This suggests that as the GDP per capita increases, the number of suicides tends to decrease slightly. However, the correlation is very weak, which means that the relationship between the two variables is not very strong or consistent.
# 
# The value 0.54 indicates a moderate positive correlation between the No of suicides and population. This suggests that as the population increases, the number of suicides also tends to increase. This is not surprising, as more people generally means more suicides, but there are many other factors that can influence suicide rates as well.
# 
# The value 0.038 indicates a weak negative correlation between GDP per capital and Population. This suggests that as the population increases, the GDP per capita tends to decrease slightly. However, the correlation is very weak, which means that the relationship between the two variables is not very strong or consistent.
# 
# From the foregoing, we can conclude that there is no strong relationship between these variables. The correlations are generally weak to moderate, which suggests that the relationship between these variables is complex and cannot be easily explained by a simple linear relationship

# #### g)Use appropriate visual notation to visualise total suicides over years. Describe your findings

# In[565]:


# group the suicide_master_df by year and sum the number of suicides
suicides_per_year = suicide_master_df.groupby('year')['suicides_no'].sum()


# In[566]:


#suicides per year index
suicides_per_year.index


# In[567]:


#suicides per year values
suicides_per_year.values


# In[568]:


# create a line chart
plt.plot(suicides_per_year.index, suicides_per_year.values)
# set the axis labels and title
plt.xlabel('Year')
plt.ylabel('Total Suicides')
plt.title('Total Suicides over Years')

plt.show()


# This visualization shows the overall trend in Total Suicides over Years, the overall number of suicides climbed consistently from 1985 to 1995, with a sharp increse in the early 1990s. Suicides then peaked in the mid-1990s before progressively dropping until about the year 2000. The total number of suicides remained largely consistent after 2000.
# 
# It is worth noting that this visualization only shows the overall trend and does not take into account any differences between countries, age groups, or other factors that may be important in understanding suicide rates. Therefore, additional analyses may be necessary to fully understand the patterns and factors associated with suicide over time.

# ####  h)Compare suicides by gender over years and state your conclusions

# In[569]:


# # group the suicide_master_df by year and gender and sum the number of suicides
suicides_gender= suicide_master_df.groupby(['year', 'sex'])['suicides_no'].sum().unstack()
suicides_gender


# In[570]:


suicides_gender.plot()
plt.xlabel('Year')
plt.ylabel('Total Suicides')
plt.title('Comparison of suicides by gender over years ')


# Based on this chart, we can observe that throughout the entire time period, males consistently had higher suicide rates than females. However, the trends in suicide rates differ between males and females over time. For males, the number of suicides increased steadily from 1985 to 1995, with a sharp increase in the early 1990s, then peaked in the mid-1990s, before gradually declining until around 2000. After 2000, the total number of suicides remained relatively stable. For females, the number of suicides increased more gradually from 1985 to 1995 and  remained relatively stablewith a peak in the late 1990s, then declined until around 2005, before gradually increasing again.
# 
# 
# From the foregoing, The graph suggests that suicide prevention and intervention initiatives for males and females, as well as different age groups and geographies, may need to be handled differently. It is also worth noting that the data shown in this visualisation is a compilation of many different countries, and it is probable that cultural, social, and economic variables influence suicide rates differently across different areas and countries. As a result, further research may be required to completely comprehend the patterns and causes related with suicide rates across time and among different populations.

# ####  i)Calculate and Visualise suicides on generation and on age group. Describe your findings.

# In[571]:


# group the suicide_master_df by generation and by age and sum sucicides_no
suicides_by_gen_age = suicide_master_df.groupby(['generation', 'age'])['suicides_no'].sum().unstack()
suicides_by_gen_age


# In[572]:


# create a bar chart
suicides_by_gen_age.plot(kind="bar")

# set the axis labels and title
plt.xlabel('Generation')
plt.ylabel('Total Suicides')
plt.title('Total Suicides by Generation and Age Group')

# show the chart
plt.show()



# In[573]:


# Let create a stacked bar chart
suicides_by_gen_age.plot(kind="bar", stacked=True)
# set the axis labels and title
plt.xlabel('Generation')
plt.ylabel('Total Suicides')
plt.title('Total Suicides by Generation and Age Group')

# show the chart
plt.show()


# Based on this chart, we can observe that the age group with the highest number of suicides is 35-54 years, followed by 55-74 years and 25-34 years. The age group with the lowest number of suicides is 5-14 years. We can also see that the Boomers and Silent generations had the highest number of suicides, while the Generation Z and the Millenials had the lowest
# 
# 
#  From the foregoing, this visualization suggests that suicide prevention and intervention efforts may need to target specific age groups and generations, with a focus on the middle-aged population. It is also important to consider the potential cultural, social, and economic factors that may be contributing to the observed patterns in suicide rates across different age groups and generations.

# In[ ]:




