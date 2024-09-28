import pandas as pd

# Sample data
data = {
    'id': [1, 2, 3, 1, 1],
    'revenue': [8000, 9000, 10000, 7000, 6000],
    'month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar']
}

# Create a dataframe
df = pd.DataFrame(data)
print("df: \n", df)
print(" ")

# Pivot the table
"""
This line of code is using the pivot_table function from pandas to reshape the DataFrame df. 
Here’s what each parameter means:
    index='id': This specifies that the id column should be used as the index of the resulting pivot table
        .Each unique value in the id column will become a row in the pivot table.
    columns='month': This specifies that the month column should be used to create new columns in the pivot table. Each
        unique value in the month column will become a column in the pivot table.
    values='revenue': This specifies that the values in the revenue column should be used to fill the cells
        of the pivot table.
    aggfunc='first': This specifies the aggregation function to use when there are multiple values for the same id 
        and month combination. In this case, first means that the first encountered value will be used.
    The result is a DataFrame where each row represents a unique id, each column represents a month, and the 
        cells contain the revenue values. If there are multiple revenue entries for the same id and
         month, only the first one is taken.
"""
pivot_df = df.pivot_table(index='id', columns='month', values='revenue', aggfunc='first')
print("pivot_df:\n", pivot_df)
print(" ")

# Rename columns to match the desired format
pivot_df.columns = [f"{month}_Revenue" for month in pivot_df.columns]
print("pivot_df: \n", pivot_df)

# Reset index to make 'id' a column again
pivot_df.reset_index(inplace=True)
print(" ")
print("pivot_df: \n", pivot_df)

# Ensure all months are present
all_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
for month in all_months:
    if f"{month}_Revenue" not in pivot_df.columns:
        pivot_df[f"{month}_Revenue"] = pd.NA
print(" ")
print("pivot_df: \n", pivot_df)

# Reorder Column
ordered_columns = ['id'] + [f"{month}_Revenue" for month in all_months]
pivot_df = pivot_df[ordered_columns]

print(" ")
print("pivot_df: \n", pivot_df)

"""
This code ensures that all month columns are present in the DataFrame, even if they were not in the original data. It
adds these columns with `NaN` values if they are missing, and then reorders the columns as required.
"""