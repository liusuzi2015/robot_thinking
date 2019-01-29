import urllib
import urllib.parse
import urllib.request
import pandas as pd

# Upload data from GitHub to notebook's local drive
url = "https://raw.githubusercontent.com/GokuMohandas/practicalAI/master/data/titanic.csv"
response = urllib.request.urlopen(url)
html = response.read()
with open('titanic.csv', 'wb') as f:
    f.write(html)

# Read from CSV to Pandas DataFrame
df = pd.read_csv("titanic.csv", header=0)
# First five items
# print(df.head())

# # Describe features
# print(df.describe())

# Histograms
df["age"].hist()