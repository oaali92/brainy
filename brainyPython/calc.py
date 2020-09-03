"""
Calculate Random Python Function for Electron App
"""

__author__ = 'Omar'


from sys import argv
import json
import os
from scipy import stats
import pandas as pd

# lets change to argparse


def main():
    fp = os.getcwd() + '\\' + argv[1]
    with open(fp, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df['balance'] = pd.to_numeric(df['balance'])
    df['age'] = pd.to_numeric(df['age'])
    slope, intercept, r_value, p_value, std_err = stats.linregress(df['balance'], df['age'])
    # print(df.head())
    print(f'y = {round(slope,4)}x + {round(intercept,4)}')

if __name__ == '__main__':
    main()
