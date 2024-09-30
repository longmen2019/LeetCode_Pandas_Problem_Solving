import pandas as pd

# Sample data

data = {
    'id': [1, 2, 3],
    'email': ['a@b.com', 'c@d.com', 'a@b.com']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Find duplicate email
# Use duplicated(subset='email', keep=False) to mark all rows with duplicate emails.
duplicate_email = df[df.duplicated(subset='email', keep=False)]

# Select only the email column and drop duplicates
# Filter the DataFrame to keep only the duplicate emails and then drop any duplicate rows in the result
result = duplicate_email[['email']].drop_duplicates()

print(result)