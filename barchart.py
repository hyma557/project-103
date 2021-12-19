import pandas as pd
import plotly.express as px

df = pd.read_csv("chart.csv")
fig = px.bar(df, x = "date", y = "cases", title = "BarChart")
fig.show()
