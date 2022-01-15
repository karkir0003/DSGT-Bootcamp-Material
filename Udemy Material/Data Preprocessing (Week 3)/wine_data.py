from sklearn.datasets import load_wine

import pandas as pd  # fill in with the proper package name 
import numpy as np

def get_wine_data():
    data = load_wine() 
    features = data.data # these are our features 
    labels = data.target
    df = pd.DataFrame(features)
    df.columns = data.feature_names
    df['labels'] = labels
    return df

def get_feature_titles():
    """
    Return the title of each feature. Recall the definition of a feature
    """
    df = get_wine_data()
    #YOUR CODE HERE
    pass

def add_2_to_magnesium():
    """
    Add 2 points to the magnesium of each entry. Return the resulting dataframe (ensure that you are returning a new dataframe)
    """
    df = get_wine_data()
    #YOUR CODE HERE
    pass

def create_flav_to_non_flav_ratio():
    """
    Create a new feature called flav_to_non_flav ratio that is the ratio between flavanoids and nonflavanoid_phenols.
    Ensure you return a df.head()
    """
    df = get_wine_data()
    #YOUR CODE HERE. Ensure you return a df.head()
    pass

def get_num_missing_values():
    """
    For each column, find the number of missing values
    """
    df = get_wine_data()
    #YOUR CODE HERE
    pass

def alcohol_content_level_sifter():
    """
    It might be possible that alcohol content might influence the label on the wine. Create a column in the dataframe called
    alcohol_content_level. If the alcohol value is over 13.5, put 1 in that entry. If the alcohol value is at most 13.5, put 
    0. For example, if alcohol value is 6, alcohol_content_level is 0. If the alcohol value is 15, alcohol_content_level is 1
    What we are doing is a type of feature encoding
    """
    df = get_wine_data()
    #YOUR CODE HERE. Return the resulting dataframe
    pass

