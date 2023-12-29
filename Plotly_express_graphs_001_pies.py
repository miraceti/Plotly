import pandas as pd
import plotly.express as px
dfb = pd.read_csv("bird-window-collision-death.csv")

df = px.data.tips()

# scatter_plot = plotly.express.scatter(data_frame=df, x="age", y="income" )

# import plotly.graph_objects as go
# scatter_plot = go.Figure(data=go.Scatter(x=df["age"], y=df["income"], mode='markers'))

print(df)
print(dfb)
fig = px.pie(dfb, values='Deaths', names='Bldg #', color="Side", hole=0.3)

fig.update_traces(textinfo="label+percent", insidetextfont=dict(color="white"))
fig.update_layout(legend={"itemclick":False})
fig.show()

fig.write_image("images/fig1.png")