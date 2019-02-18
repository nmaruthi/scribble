#Program with a custom function to
#count the frequency of values in a column
#Practicing lessons from Datacamp

import pandas as pd

def colFreqCounter(df, colName):
    """Method to count the frequency of values in a column"""
    col=df[colName]
    freqDict={}

    for item in col:
        if item in freqDict.keys():
            freqDict[item] += 1
        else:
            freqDict[item] = 1

    return freqDict

tweets_df=pd.read_csv("C:/myStuff/Documents/OSU/osu_notes/python/workspace/scribble/datasets/tweets.csv")
print(colFreqCounter(tweets_df,'lang'))

#Output:
#{'en': 97, 'et': 1, 'und': 2}