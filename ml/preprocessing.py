import pandas as pd


data = pd.read_csv('data/raw.csv')
data = data.drop_duplicates(subset=['title'], keep='first')
data = data.drop(columns=["doi", "updated", "affiliation"])


data.to_csv('data/cleaned.csv', index=False)