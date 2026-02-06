# Import pandas for data manipulation as we did earlier
import pandas as pd
# and import Dash for webapp , html and dcc for graphs and sliders
# Will use input and output for callback 
from dash import Dash, html, dcc , Input, Output
# import plotly libraries for visually appealing graphs
import plotly.express as px
import plotly.graph_objects as go

# Now we will read pink_morsel_sales.csv
df = pd.read_csv(r"data/pink_morsel_sales.csv")
#print(df.head())

# Lets rename the columns for ease
df = df.rename(columns={'date':'Date', 'product':'Product', 'region':'Region', })
#print(df.head())

# Now will format date for use 
df['Date'] = pd.to_datetime(df['Date'])
#print(df.head())

# Now will calculate daily sales for the product
daily_sales = df.groupby('Date', as_index=False)['Sales'].sum()
#print(daily_sales.head())

#Now we divide the daily_sales according to each region
# Which i forget in the last commit and it will be used for 
# Region picker in the graph 
daily_region_sales = df.groupby(
    ['Date', 'Region'], as_index=False)['Sales'].sum()
#Calculate lowest and higehst sales in a day for all regions combine


Lowest_sales = daily_sales.loc[daily_sales['Sales'].idxmin()]
Highest_sales = daily_sales.loc[daily_sales['Sales'].idxmax()]
#print(Lowest_sales)
#print(Highest_sales)
#High_for_one_region = daily_region_sales.loc[daily_region_sales['Sales'].idxmax()]
#print("High_for_one_region")
#print(High_for_one_region)

#Low_for_one_region = daily_region_sales.loc[daily_region_sales['Sales'].idxmin()]
#print("Low_for_one_region")
#print(Low_for_one_region)
# Now we will check if sales increased after price increase date

# Price increase date
price_increase_date = pd.to_datetime('2021-01-15')
#print(price_increase_date)

# Before vs after the price_increase_date
before_price_increase = daily_sales[daily_sales['Date'] < price_increase_date]
after_price_increase = daily_sales[daily_sales['Date'] >= price_increase_date]

#print(before_price_increase)
#print(after_price_increase)

# Now we can view from dataset that sales increases after the price_increase date but we will make a function
conclusion = ('Sales increased after price increase date'
               if after_price_increase['Sales'].sum() > before_price_increase['Sales'].sum() 
               else 'Sales decreased after price increase date')
print("Conclusion:", conclusion)

#


# Now we will make Dash app for visualization

app = Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualization", style={'text-align': 'center'}),
    # Added Radio items for selection of regions
    dcc.RadioItems(
    id='region-picker',
    options=[
        {'label': 'All Regions', 'value': 'all'},
        {'label': 'North', 'value': 'north'},
        {'label': 'South', 'value': 'south'},
        {'label': 'East', 'value': 'east'},
        {'label': 'West', 'value': 'west'},
    ],
    value='all',
    inline=True,
    style={'text-align': 'center', 'margin-bottom': '20px'}
),
    dcc.Graph(id='sales-graph')
])
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):

    if selected_region == 'all':
        #plot_df is used to store the selected dataframe now
        plot_df = daily_sales
    else:
        plot_df = daily_region_sales[
            daily_region_sales['Region'].str.lower() == selected_region
        ]
   
    highest_row = plot_df.loc[plot_df['Sales'].idxmax()]
    lowest_row = plot_df.loc[plot_df['Sales'].idxmin()]
#Now time to structure of line chart
    fig = px.line(
    # fixed the bug 
    # I was using plot_df instead of daily_sales
    plot_df,
    x='Date',
    y='Sales',
    labels={'Date': 'Date', 'Sales': 'Total Daily Sales'},
    )
    fig.update_layout(
    title="Pink Morsel — Daily Sales Trend",
    title_x=0.5,
    template="plotly_white",
    margin=dict(l=40, r=40, t=60, b=40),
    )
# Price increase marker
    fig.add_vline(
    x=price_increase_date.strftime("%Y-%m-%d"),
    line_dash="dash",
    line_color="crimson"
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
    x=[highest_row['Date']],
    y=[highest_row['Sales']],
    mode='markers',
    marker=dict(size=9),
    name="Highest Sales Day"
    ))
    fig.add_trace(go.Scatter(
    x=[lowest_row['Date']],
    y=[lowest_row['Sales']],
    mode='markers',
    marker=dict(size=9),
    name="Lowest Sales Day"
    ))
    return fig

if __name__ == '__main__':
    app.run(debug=True)
