import plotly.express as px

df = px.data.tips()
fig = px.sunburst(df, path=['day', 'time', 'sex'], values='total_bill')

config = {
    "displaylogo": False,
}
fig.write_html('../vis_html/pie_chart_demo.html', config=config, auto_open=False)

