import pandas as pd

#Reading a CSV file
brics=pd.read_csv(data_sets_path+separator+'brics.csv', index_col=0)

#Subsetting the data frame to specific rows & columns
#This returns a data frame since double-square brackets are used
brics.loc[['RU', 'IN', 'SA'], ['country', 'capital']]