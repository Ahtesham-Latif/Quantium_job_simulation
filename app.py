# Import pandas library
import pandas as pd
# Load all CSV files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Contactenate all dataframes into a single dataframe
# We will use ignore_index=True to reset the index in the concatenated dataframe
# Means the indecies will not look like  0,1,2 and then 0,1,2 again for the next dataframe
df = pd.concat([df0,df1,df2], ignore_index=True)

# Lets display the first 5 rows of the dataframe
print(df.head())
# Lets display the last 5 rows of the dataframe
print(df.tail())
# Display the shape of the dataframe
print("Shape of the dataframe:", df.shape)
# Display the column names of the dataframe
print("Column names:", df.columns.tolist())

# Now will choose only pink morsel from product columns
pink_morsel_df = df[df['product'].str.lower() == 'pink morsel']
print("Pink Morsel Dataframe:")


# Now we need to convert price to float for calculation
pink_morsel_df['price'] = pink_morsel_df['price'].replace('[\$,]', '', regex=True).astype(float)    
print(pink_morsel_df.head())
# Lets here check the shape of pink morsel dataframe for verification of total records
print("Shape of Pink Morsel Dataframe:", pink_morsel_df.shape)
# Now we will calculate total sales for pink morsel
total_sales_pink_morsel = pink_morsel_df['price'] * pink_morsel_df['quantity']
print("Total sales for Pink Morsel:", total_sales_pink_morsel.sum())

# Now we will merge the the price and quantity columns to get total sales column
pink_morsel_df['Sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']
print("Pink Morsel Dataframe with Total Sales:", pink_morsel_df.head())

# Now we will stoere this pink morsel dataframe to a csv file 
# But before that only keep relevant columns

pink_morsel_df = pink_morsel_df[['product', 'Sales', 'date',  'region']]

pink_morsel_df.to_csv("data/pink_morsel_sales.csv", index=False)

print("Pink Morsel sales data saved to pink_morsel_sales.csv")
print(pink_morsel_df.head())

df_morsel = pd.read_csv(r"data/pink_morsel_sales.csv")
print(df_morsel.head())