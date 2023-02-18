import plotly.graph_objs as go


def plot_candlestick(df):
    fig = go.Figure(
        data=[go.Candlestick(x=df.index,
                             open=df['Open'],
                             high=df['High'],
                             low=df['Low'],
                             close=df['Close'])],
        layout=go.Layout(title=go.layout.Title(text='Candlestick Chart'))
    )

    fig.show()

