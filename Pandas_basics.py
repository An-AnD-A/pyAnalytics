# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 01:19:41 2021

@author: Anand A
"""
### Working on Pandas basics.

# import the necessary libraries

import pandas as pd
import numpy as np

# importing the dataset.

df = pd.read_csv("C:/analytics/datasets/developer_survey_2020/survey_results_public.csv")

df_schema = pd.read_csv('C:/analytics/datasets/developer_survey_2020/survey_results_schema.csv')

# Viewing imported data

df.shape    # no parenthesis as shape is an attribute not a method.

df.info()   # gives more info on each column. gives the datatype for each column,

df.head(10) # Gives first 10 rows. (default value is 5.)

df.tail(10) # Gives the last 10 rows. (default value os 5.)

# Making a dataframe with dictionary

data = {"First name": ["Nathan","Matej","Ondrej","Ethan","Will","Ethan"],
        "Last name": ["Bishop","Kovar","Mastny","Laird","Fish","Galbraith"],
        "Position": ["GK","GK","GK","DEF","DEF","MID"],
        "Age": ["20","21","19","20","18","20"],
        "Nationality": ["England","Czech Republic","Czech Republic","England","England","Northern Ireland"]}

Players = pd.DataFrame(data)

# Accessing one column series from a dataframe.

Players["Age"]         # Preferred way to access columns

Players.Age            # Not preferred as sometimes the Column names might be same as an attribute.

# NOTE: Each column of a dataframe data structure is a series.

Players[["First name","Last name"]] # Calling multiple columns simultaneously. The output is a dataframe and not a series

# Accessing rows from a dataframe. 

Players.loc[[0,1],["First name","Last name"]] # using the row and column index.

Players.iloc[[0,1],[0,1]]   # Using the integer location

# Accessing a list of all the columns in a dataframe.

df.columns             # Gives all the column indeces.

# Accessing the hobbyist column from our dataset.

df["Hobbyist"]  # Gives a series

df["Hobbyist"].value_counts() # value_counts method gives the No. of times each value appear in that column.

df.loc[[0,1,2],"Hobbyist"] # getting the first 3 rows from the hobbyist column.

df.loc[0:2, "Hobbyist":"Employment"] # when using slicing we are not passing a list.

# NOTE : While slicing in dataframe the end index is also inclusive.

## SETTING INDEX VALUES

Players.index  # Gives as a List
df.index       

Players.set_index("Position",inplace = True) # Setting the row index as a column in dataframe.

# by default the index change is not permanent. we need to specify inplace = True to make it permanent.

Players.loc["GK"]    # Note that the index need not be unique values.

Players.index

Players.reset_index(inplace = True) # To reset the index to default range. Usually the default is 0,1,...

# Changing the dataset index to respondent ID.

df.set_index("Respondent", inplace = True)
df.reset_index(inplace = True)

# NOTE: we can set the index when we called the csv file.

df = pd.read_csv("C:/analytics/datasets/developer_survey_2020/survey_results_public.csv",index_col = "Respondent")

# Setting the index values of schema dataset as the column names.

df_schema = pd.read_csv('C:/analytics/datasets/developer_survey_2020/survey_results_schema.csv',index_col='Column')

df_schema.loc["Hobbyist"]
df_schema.loc["NEWEdImpt","QuestionText"]  # NOTE: Pass the column name too to get the full text

# Sorting the index

df_schema.sort_index() # Sort the index alphabetically.
df_schema.sort_index(ascending = False) # Sort the index in descending manner.

# Note: we have to specify inplace = True to make these changes permanent.

## FILTERING DATA

Players[Players["Nationality"] == "Czech Republic"]
filt1 = Players["Nationality"] == "England" # better to assign a variable to the condition.
Players.loc[filt1] # Players[filt1] also gives same but better to use .loc as we can give column index too.
Players.loc[filt1,"Last name"]

# Using multiple conditions

filt2 = (Players["Position"] == "GK") & (Players["Nationality"] == "England") 
Players.loc[filt2,["First name","Last name"]]

# NOTE : When giving multiple conditions parenthesis should be given to nsure booleans are performed initially.

# An easy way to get the opposite of filt booleans is to add a tilda in front of filt while passing in loc.

Players.loc[~filt2,["First name","Last name"]]

# Filtering on stack Overflow survey dataset.

filt3 = (df["Country"] == "India") & (df["ConvertedComp"] > 50000)

df.loc[filt3]

# Filtering all the respondents that is from India and uses Python and then finding their income.

filt4 = (df["Country"] == "India") & (df["LanguageWorkedWith"].str.contains("Python",na = False)) & (df["ConvertedComp"] > 30000)

df.loc[filt4]

# NOTE : Conditions will give a Boolean Series as the output. We can pass the Boolean Series to get desired values from the DataFrame.

## UPDATING ROW AND COLUMN

# Updating and editing column index.

Players.columns

# we can give the column index as a list.

Players.columns = ['Position', 'First name', 'Last name', 'Age', 'Nationality']
Players

#Editing column index

Players.columns = [x.upper() for x in Players.columns] # Using List Comprehension.
Players

Players.columns = [x.replace(" ","_") for x in Players.columns]
Players

Players.columns = Players.columns.str.replace("_"," ") # Alternate method 
Players

Players.columns = Players.columns.str.lower() # Alternate method 
Players

#Changing individual column index.

#Renaming using dictionary. keys - current index and value - new xolumn index value

Players.rename(columns = {"first name" : "First name",
                          "last name"  : "Last name",
                          "position"   : "Position",
                          "age"        : "Age",
                          "nationality": "Nationality"},inplace = True) 

#Chnaging specific values

Players.loc[4,["First name","Last name"]] = ["Fish","Will"]
Players

Players.loc[4,"First name"] = "Will"
Players.at[4,"Last name"] = "Fish"  # For single value changes we can use at method too.

# Change an entire column to upper case

Players["Nationality"] = Players["Nationality"].str.upper()
Players

# Using the apply method to perform a function on a column in dataframe.

## NOTE: Apply works differently on Series and Dataframe

#Apply on Series objects.
def case_lower(st):
    return st.lower()
    
Players["Nationality"] = Players["Nationality"].apply(case_lower)
Players

Players["Nationality"] = Players["Nationality"].apply(lambda x : x.upper())
Players

# Difference in apply when using Series and Dataframe 

Players["First name"].apply(len)  # Gives the length of each element in first name series.

Players.apply(len)  # gives the length of each column in dataframe
Players.apply(len, axis = "columns") # gives the length of each rows.(axis = "columns" is same as  axis = 1)

# Get the minimum value in each column

Players.apply(pd.Series.min)
Players.apply(lambda x : x.min())  # The x in this case is a series so we apply a series method .min()

## NOTE : Runing apply to series apply the function to each element of series.
##        Runing apply to a dataframe apply the function to each columnseries in the dataframe

# applymap method is used to apply a function on all the elements in a dataframe.

Players.applymap(len) # gives length of each element in the datframe. If non string elements are present can give errors.

# map method is used to substitute elements in a series.

Players["First name"].map({"Nathan" : "Nat","Ethan" : "Eth", "Will": "Wi"})

## The elements that are not given substitute values are assigned as NaN.

# replace method is used when we just want to replace one or two elements in the series and not change rest of the elements.

Players["First name"].replace({"Nathan":"Nat","Ethan" : "Eth","Will":"Wi"})

## Working on real dataset

# Change the ConvertedComp column name to Salary in USD

df.rename(columns = {"ConvertedComp" : "Salary_in_USD"},inplace = True)

# Change Hobbyist colums such that Yes becomes True and No becomes False.

df["Hobbyist"].map({"Yes" : True,"No" : False})

# there is no inplace argument for map so use assignment to make changes permanent.

df["Hobbyist"] = df["Hobbyist"].map({"Yes" : True,"No" : False})

## ADDING AND REMOVING COLUMNS

# add a column

Players["Full name"] = Players["First name"] + ' ' + Players["Last name"]
Players

# Removing columns

Players.drop(columns = ["First name","Last name"],inplace =  True)

# Making column from existing columns

Players["Full name"].str.split(" ", expand = True) # split gives a list while expand true will give a dataframe made of the list.

Players["Full name"].apply(lambda x : x.split())  # Split using lambdas

Players[["First name", "Last name"]] = Players["Full name"].str.split(" ", expand = True)
Players

# Making and editing rows.

Players.append({"First name" : "D'Mani","Position": "FWD"},ignore_index = True)
# The ramaining columns are provided as NaN.

# Removing a column. (Method 2)

Players.drop(index=6,axis="rows")
Players

# Joining two dataframes

dict2    = {"First name" : ["D'Mani","Dillon","Mateo"],
            "Last name"  : ["Mellor","Hoogewerf","Mejia"],
            "Position"   : ["FWD","FWD","FWD"],
            "Age"        : ["20","18","18"],
            "Nationality": ["England","Netherlands","Spain"]
            }

Players2 = pd.DataFrame(dict2)
Players2["Full name"] = Players2["First name"] + " " + Players2["Last name"]

Players = Players.append(Players2,ignore_index =True,sort=False)
Players
# Remove a row based on a condition.

filt5 = Players[Players["Last name"] == "Kovar"].index

Players = Players.drop(filt5)

Players.reset_index(inplace = True,drop = True) 

# drop = True ensures that the previous index is not added as a column in the datframe.

Players


## SORTING DATA

df = pd.read_csv("C:/analytics/datasets/developer_survey_2020/survey_results_public.csv")
df.rename(columns = {"ConvertedComp" : "Salary_in_USD"},inplace = True)
# Using sort_values method.

Players.sort_values(["Position","First name","Last name"], ascending = [True,True,False],inplace = True)
Players

# Using sort_index method

Players.sort_index(inplace = True)
Players

# Working with stack overflow data

df.sort_values(by =["Country","Salary_in_USD"], ascending = [True, False],inplace = True)
df[["Country","Salary_in_USD"]]

## GROUPING AND AGGREGATING

df["Hobbyist"] = df["Hobbyist"].map({True : "Yes", False : "No"})
df["Hobbyist"]

df["Salary_in_USD"].describe()
df["Salary_in_USD"].median()

df.median()        # median of all columns with numerical values.
df.describe()

# count and value_count methods

df["Hobbyist"].count()  # gives the total number of responses.(not including NaN)

df["Hobbyist"].value_counts() # gives the number of each response.

df["EdLevel"].value_counts(normalize = True)*100 # gives percentage of each response
df["Country"].value_counts()


# groupby method 

# NOTE: groupby involves - splitting an object, applying a function and the regrouping

country_grp = df.groupby(["Country"]) # generate a Dataframe.groupby object

country_grp["EdLevel"].value_counts() # count no. of each response for the column in each group.

country_grp["Gender"].value_counts() 

# Once the function is applied it is a Series object.

country_grp["EdLevel"].value_counts(normalize = True).loc["India"] # getting one group from the object

country_grp.get_group("India")["Gender"].value_counts() # 2nd way (more complex)

# NOTE: In first way we are finding for all countries while in 2nd we do it for only one country.

country_grp["Salary_in_USD"].median().loc["India"]

# Using aggregate function.

country_grp["Salary_in_USD"].agg(["median","mean"])

# apply method
# How many people in each country knows how to use Python

resp_py = country_grp["LanguageWorkedWith"].apply(lambda x: x.str.contains("Python").sum()).sort_values(ascending = False)

resp_tot = country_grp["Respondent"].count().sort_values(ascending = False)

type(resp_py)
type(resp_tot)

df_py_user = pd.concat([resp_tot,resp_py],axis = "columns",sort= False)
df_py_user.rename(columns = {"LanguageWorkedWith" : "Python Users"},inplace = True)

df_py_user["Percentage of Python users"] = (df_py_user["Python Users"]/df_py_user["Respondent"])*100

df_py_user.sort_values(by = ["Percentage of Python users"],ascending = False, inplace = True)

# CLEANING DATA

Players

Players3 = pd.DataFrame({"Position"   : ["MID","MID","Missing"] ,
                         "First name" : ["Dylan","Martin","NA"],
                         "Last name"  : ["Levitt","Svidersky","Missing"]} )
Players.loc[8,"Age"] = 20

Players = Players.append(Players3,ignore_index = False, sort = False)
Players.reset_index(drop = True,inplace = True)

# dropping missing data rows.

Players.dropna(axis = "rows",how="any") # remove all rows with any column value as NaN
Players.dropna(axis = "rows",how="all") # remove all rows with all column value as NaN

Players.dropna(axis = "columns",how="all") # remove all columns with all row value as NaN

Players.dropna(axis = "rows",how="any",subset=["First name","Last name","Age"]) # rows dropped if all subset columns are missing.

# Add inplace argument for making the changes permanent

# Replace the custom missing values

Players.replace({"Missing" : np.nan,"NA" : np.nan}, inplace = True)
Players                 

# isna and fillna methods

Players.isna()              # Shows all the na values as a boolean series 
Players.fillna("MISSING")   # Fills all the na values with the value we want.

    #pd.notna()
    #pd.empty()
    #pd.axes()
    #pd.ndim()
    #pd.at()
    #pd.iat()
    #pd.filter()
    #pd.kurt()
    #pd.mean()
    #pd.rank()
    #pd.series.unique()
    #df.query()
    
# NOTE: We can pass an argument of a list of custom missing data while reading the csv file.

## Casting data

Players.dtypes

# We need to convert the age to a float before finding the mean age
Players["Age"] = Players["Age"].astype(float)
Players["Age"].mean()

# NOTE: Converting to an integer causes erroe when NaN values are present. Hence float is used.

