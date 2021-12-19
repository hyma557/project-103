import pandas as pd 
import plotly.express as px

df = pd.read_csv("chart.csv")
fig = px.line(df,x = "data", y = "cases", color = "country", title = "Corona cases")
fig.show()