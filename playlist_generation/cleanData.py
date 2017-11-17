import pandas as pd

df = pd.read_csv('../data/song_data.csv')
df = df.drop_duplicates(subset = ['songid'], keep = 'first')
df.to_csv('../data/song_data_unique.csv', sep = ',', encoding = 'utf-8', index = False)
