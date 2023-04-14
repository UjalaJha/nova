import pandas as pd

df_apache = pd.read_csv("repos_apache-2.0.csv")
print(df_apache.head())
print(df_apache.count())

df_mit = pd.read_csv("repos_mit_old.csv")
print(df_mit.head())
print(df_mit.count())