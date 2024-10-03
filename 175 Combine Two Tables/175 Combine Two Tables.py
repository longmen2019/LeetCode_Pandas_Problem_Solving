import pandas as pd

# Sample data for Person table
person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}

# Sample data for Address table
Address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}

# Create a DataFrames
person_df = pd.DataFrame(person_data)
address_df = pd.DataFrame(Address_data)

# Perform left join
result_df = pd.merge(person_df, address_df, on= 'personId', how='left')

# Select and reorder columns
result_df = result_df[['firstName', 'lastName', 'city', 'state']]

print(result_df)