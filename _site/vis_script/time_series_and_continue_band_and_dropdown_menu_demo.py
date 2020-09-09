import plotly.graph_objects as go


# Load dataset
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# Initialize figure
fig = go.Figure()

# Add Traces
fig.add_trace(
    go.Scatter(
        name='ground truth',
        x=df['Date'], 
        y=df['AAPL.Adjusted'],
        mode='lines',
        # line=dict(color='rgb(31, 119, 180)'),
    )
)

# model 1
fig.add_trace(
    go.Scatter(
        name='model1 predictions',
        x=df['Date'], 
        y=df['mavg'],
        mode='lines',
        # line=dict(color='rgb(31, 119, 180)'),
    )
)
fig.add_trace(
    go.Scatter(
        name='model1 Upper Bound',
        x=df['Date'],
        y=df['up'],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    )
)
fig.add_trace(
    go.Scatter(
        name='model1 Lower Bound',
        x=df['Date'],
        y=df['dn'],
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
)

# model 2
fig.add_trace(
    go.Scatter(
        name='model2 predictions',
        x=df['Date'], 
        y=df['AAPL.Open'],
        mode='lines',
        visible=False,
        # line=dict(color='rgb(31, 119, 180)'),
    )
)
fig.add_trace(
    go.Scatter(
        name='model2 Upper Bound',
        x=df['Date'],
        y=df['AAPL.High'],
        mode='lines',
        visible=False,
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    )
)
fig.add_trace(
    go.Scatter(
        name='model2 Lower Bound',
        x=df['Date'],
        y=df['AAPL.Low'],
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        visible=False,
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
)

# Add Annotations and Buttons
model1_annotations = [
    dict(x=1,
         y=df['up'].max(),
         xref="paper", yref="y",
         text="Model 1 is XXX ...<br> It's XXX is %.3f" % df['up'].max(),
         align="right",
         showarrow=False,
         ax=0, ay=-40)
]
model2_annotations = [
    dict(x=1,
         y=df['AAPL.High'].max(),
         xref="paper", yref="y",
         text="Model 2 is XXX ...<br> It's XXX is %.3f" % df['AAPL.High'].max(),
         align="right",
         showarrow=False,
         ax=0, ay=-40)
]


fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label="Model 1",
                     method="update",
                     args=[{"visible": [True, True, True, True, False, False, False]},
                           {"title": "Model 1",
                            "annotations": model1_annotations}]),
                dict(label="Model 2",
                     method="update",
                     args=[{"visible": [True, False, False, False, True, True, True]},
                           {"title": "Model 2",
                            "annotations": model2_annotations}]),
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, False, False, True, False, False]},
                           {"title": "All Models",
                            "annotations": []}]),
            ]),
        )
    ]
)

fig.update_layout(
    yaxis_title='XXXXXX',
    title='Model 1',
    annotations=model1_annotations,
    hovermode="x"
)

config = {
    "displaylogo": False,
}
fig.write_html('../vis_html/time_series_and_continue_band_and_dropdown_menu_demo.html', config=config, auto_open=False)