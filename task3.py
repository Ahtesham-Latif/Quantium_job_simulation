# Import pandas for data manipulation as we did earlier
import pandas as pd
# and import Dash for webapp , html and dcc for graphs and sliders
from dash import Dash, html, dcc
# import plotly libraries for visually appealing graphs
import plotly.express as px
import plotly.graph_objects as go

# Now we will read pink_morsel_sales.csv
df = pd.read_csv(r"data/pink_morsel_sales.csv")
print(df.head())

# Lets rename the columns for ease
df = df.rename(columns={'date':'Date', 'product':'Product', 'region':'Region', })
print(df.head())

# Now will format date for use 
df['Date'] = pd.to_datetime(df['Date'])
print(df.head())

# Now will calculate daily sales for the product
daily_sales = df.groupby('Date', as_index=False).sum()
print(daily_sales.head())

#Calculate lowest and higehst sales in a day for all regions combine


Lowest_sales = daily_sales.loc[daily_sales['Sales'].idxmin()]
Highest_sales = daily_sales.loc[daily_sales['Sales'].idxmax()]
print(Lowest_sales)
print(Highest_sales)

# Price increase date
price_increase_date = pd.to_datetime('2021-01-15')
print(price_increase_date)

# Before vs after the price_increase_date
before_price_increase = daily_sales[daily_sales['Date'] < price_increase_date]
after_price_increase = daily_sales[daily_sales['Date'] >= price_increase_date]

print(before_price_increase)
print(after_price_increase)

# Now we can view from dataset that sales increases after the price_increase date but we will make a function
conclusion = ('Sales increased after price increase date'
               if after_price_increase['Sales'].sum() > before_price_increase['Sales'].sum() 
               else 'Sales decreased after price increase date')
print("Conclusion:", conclusion)


#Now time to structure of line chart
fig = px.line(
    daily_sales,
    x='Date',
    y='Sales',
    labels={'Date': 'Date', 'Sales': 'Total Daily Sales'},
)
fig.update_layout(
    title="Pink Morsel — Daily Sales Trend",
    # Wrote the Key insights we were looking in a more cleaner way without changing the line graph daily sales
    title_x=0.5,
    template="plotly_white",
    margin=dict(l=40, r=40, t=60, b=110),
    annotations=[
        dict(
            text=(
                "<b style='color:#1f2937'>Key Insight:</b> "
                "<b style='color:#059669'>Sales increased after the 15 Jan 2021 price rise.</b> "
                "Peak daily sales occurred <b>post-increase</b>, "
                "indicating <b style='color:#2563eb'>strong demand and price resilience</b>."
            ),
            x=0.5,
            y=-0.30,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="center",
            font=dict(size=13)
        )
    ]
)


# Price increase marker
fig.add_vline(
    x=price_increase_date.strftime("%Y-%m-%d"),
    line_dash="dash",
    line_color="magenta"
)
fig.add_annotation(
    x=price_increase_date,
    y=daily_sales['Sales'].max(),
    text="Price Increase<br>15 Jan 2021",
    showarrow=False,
    yanchor="bottom"
)
# Highest & Lowest points
fig.add_trace(go.Scatter(
    x=[Highest_sales['Date']],
    y=[Highest_sales['Sales']],
    mode='markers',
    marker=dict(size=9),
    name="Highest Sales Day"
))
fig.add_trace(go.Scatter(
    x=[Lowest_sales['Date']],
    y=[Lowest_sales['Sales']],
    mode='markers',
    marker=dict(size=9),
    name="Lowest Sales Day"
))

# Now we will make Dash app for visualization

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("Pink Morsel Sales", style={'text-align': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)


