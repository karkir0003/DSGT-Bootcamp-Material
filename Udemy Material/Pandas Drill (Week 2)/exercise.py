import pandas as pd
import numpy as np

def get_dataframe(csvFile="titanic_train.csv"):
    return pd.read_csv(csvFile)

def get_age_class_sex():
    """
    I want to find a dataframe that lists just the Age, Pclass, and Sex. Return a DataFrame with these columns
    """
    df = get_dataframe()
    #YOUR CODE HERE
    pass

def get_age_class_sex_over_30():
    """
    Suppose I want the same 3 features, but this time, I only want to see people above the age of 30.
    Ultimately I would likevisual of people over thirty, but let's just focus on getting a dataframe for now.
    """
    df = get_dataframe()
    #YOUR CODE HERE
    pass

def get_100th_person_info():
    """
    I want to access the data of the 100th person, how would I do that?
    """
    df = get_dataframe()
    #YOUR CODE HERE
    pass


def calc_num_unique_ages():
    """
    Time to go back to the main dataframe, I would like to see how many unique ages there were, what function can I use to
    find that?
    """
    df = get_dataframe()
    #YOUR CODE HERE
    pass

def get_cabin_nulls_and_shape():
    """
    I was going through the dataframe and noticed cabin had a lot of null values, how can I see how many null values there
    are? While I'm at it, let me see how big this dataframe is as a whole.
    
    This function should return a tuple of the form (number of null values in Cabin column, how many rows in the dataframe)
    """
    df = get_dataframe()
    #YOUR CODE HERE
    pass

def drop_cabin_col():
    """
    The Cabin column seems to have a lot of missing values. Drop this column and return the resulting dataframe
    """
    df = get_dataframe()
    #YOUR CODE HERE
    pass
  
def survived_within_class():
    """
    For each Pclass, return the proportion of people who survived. Round answer to nearest 3 decimal places
    Return tuple in the format (Pclass 1 survival proportion, Pclass 2 survival proportion, Pclass 3 survival proportion)
    If there is a ZeroDivisionError, return (-1,-1,-1)
    """
    df = get_dataframe()
    #YOUR CODE HERE
    pass
