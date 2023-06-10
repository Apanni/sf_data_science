import pandas as pd
melb_df = pd.read_csv('data/melb_data_fe.csv')
melb_df.groupby(by='Type').mean()