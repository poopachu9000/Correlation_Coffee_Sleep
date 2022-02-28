import csv
import plotly.express as px
import pandas as pd
import numpy as np

def plot_fig(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = 'coffee', y = 'sleep', title = 'Correlation between Coffee and Sleep')
        fig.show()  
def get_data(data_path):
    coffee_consumed = []
    sleep_slept = []
    with open(data_path) as csv_file:
        df1 = csv.DictReader(csv_file)
        for row in df1:
            coffee_consumed.append(float(row['coffee']))
            sleep_slept.append(float(row['sleep']))
    return{'x':coffee_consumed, 'y': sleep_slept}
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'], data_source['y'])
    print('Correlation between Coffee and Sleep', correlation[0,1])
def main():
    data_path = '/Users/jamespalanca/Desktop/python/testFolder/coffee.csv'
    data_source = get_data(data_path)
    findCorrelation(data_source)
    plot_fig(data_path)
main()