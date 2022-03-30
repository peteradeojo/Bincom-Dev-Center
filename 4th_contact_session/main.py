#!python

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Regex for matching patterns in data that determine whether a row will be dropped
regex = r"^(\d{2,3})(\.)?(\d{2})?"


def is_number(x):
    '''
        Takes a word and checks if Number (Integer or Float).
    '''
    try:
        # only integers and float converts safely
        num = float(x)
        return True
    except ValueError as e:  # not convertable to float
        return False


df = pd.read_csv('./incd.csv')
df.set_index(' FIPS', inplace=True)

# Extracting relevant data columns
extr = df['Average Annual Count'].str.extract(r"^(\d+)", expand=False)
extr

df['Average Annual Count'] = pd.to_numeric(extr)

working_df = df[[
    'Age-Adjusted Incidence Rate(�) - cases per 100,000',
    'Average Annual Count'
]].loc[
    df['Age-Adjusted Incidence Rate(�) - cases per 100,000'].apply(is_number)]

working_df.rename(
    columns={
        'Age-Adjusted Incidence Rate(�) - cases per 100,000': 'AAIRC',
        'Average Annual Count': 'AAC',
    },
    inplace=True
)

# Fitting the model
model = LinearRegression()
X = np.array(working_df['AAIRC'])
X = X.reshape(-1, 1)
y = np.array(working_df['AAC'])
model.fit(X, y)

r_sq = model.score(X, y)
print("Co-efficient of determination:", model.coef_)
print("intercept:", model.intercept_)
print("Model score:", r_sq)
