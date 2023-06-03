# Archivo de prueba

print("Hello World.")

## Datos simulados 

import pandas as pd

# Create a list of 6 variables
variables = ['Name', 'Age', 'Gender', 'City', 'State', 'Zip Code']

# Create a list of 30 cases
cases = [
    {'Name': 'John Doe', 'Age': 30, 'Gender': 'Male', 'City': 'San Francisco', 'State': 'California', 'Zip Code': 94105},
    {'Name': 'Jane Doe', 'Age': 25, 'Gender': 'Female', 'City': 'New York', 'State': 'New York', 'Zip Code': 10001},
    {'Name': 'Mike Smith', 'Age': 40, 'Gender': 'Male', 'City': 'Chicago', 'State': 'Illinois', 'Zip Code': 60601},
    # ...
]

# Create a dataframe
df = pd.DataFrame(cases, columns=variables)

# Set the index to the `Name` column
df.set_index('Name', inplace=True)

# Print the dataframe
print(df)