import pandas as pd
import numpy as np
# import dash as ds
# from dash import html
# from dash import dcc
# import plotly.express as px

# 1. height vs position
# 2. avg value of players from different countries
# 3. leagues comparison(value)

data = pd.read_csv("transfermarkt_fbref_201920.csv", sep=";")
pd.head(data)