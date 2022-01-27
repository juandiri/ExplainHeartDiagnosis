import csv
import os
import sys

import numpy as np
import pandas as pd

from tqdm import tqdm


def main():

    data_dir = "/home/juandiri/TFM/Project/ProcessedData/V2/LongBeach.csv"
    save_dir = "/home/juandiri/TFM/Project/ProcessedData/V3/"
    out_dir = "/home/juandiri/TFM/Project/Sample/LongBeach"

    # Dataframe to store the data
    features = ['num','id','age','sex','cp','trestbps','htn','chol','fbs','restecg','ekgmo','ekgday','ekgyr','dig','prop','nitr','pro','diuretic','proto','thaldur','met','thalach','thalrest','tpeakbps','tpeakbpd','trestbpd','exang','xhypo','oldpeak','rldv5e','cmo','cday','cyr', 'lmt','ladprox','laddist','cxmain','rcaprox','rcadist']
    matrix_dataframe = pd.DataFrame(columns=features)

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            with open(f"{data_dir}/{file}", "r") as f:
                matrix_dataframe = pd.read_csv(data_dir)
        
            # Set conditions on the number of vessels damage to extract the target column
            conditions = [
                (matrix_dataframe['num'] == 0),
                (matrix_dataframe['num'] == 1),
                (matrix_dataframe['num'] > 1)
            ]
            values = [0, 1, 2]

            matrix_dataframe['target'] = np.select(conditions, values)

            # Select integer and float type columns
            numerical_columns = ['trestbps','chol','ekgmo','ekgday','ekgyr','thaldur','met','thalach','thalrest','tpeakbps','tpeakbpd','trestbpd', 'oldpeak','rldv5e','cmo','cday','cyr', 'lmt','ladprox','laddist','cxmain','rcaprox','rcadist']

            # Replace 0 values in those columns with placeholder
            matrix_dataframe[numerical_columns] = matrix_dataframe[numerical_columns].replace(0, -1440)
            

            # Replace NaN values with place holder
            matrix_dataframe = matrix_dataframe.replace(np.NaN, -1440)

            # Drop duplicate rows
            matrix_dataframe = matrix_dataframe.drop_duplicates()

            # Saving the data
            matrix_dataframe.to_csv(f"{out_dir}/D.csv", index=False)
            matrix_dataframe.to_csv(f"{save_dir}/{out_dir.split('/')[-1]}.csv", index=False)    
             


if __name__ == '__main__':
    if len(sys.argv[1:]) != 0:
        print("There are some parameters of the function are missing.")
        print((sys.argv[1:]))
        exit(1)
    main(*sys.argv[1:])
