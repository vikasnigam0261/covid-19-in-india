import pandas as pd

x = pd.read_csv('covid_data.csv')
x.to_json('covid_d.json')