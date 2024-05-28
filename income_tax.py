import pandas as pd

# Load the CSV file
file_path = 'Income_tax.csv'
data = pd.read_csv(file_path, skiprows=2)

data.columns = ['Year', 'Month', 'Day', 'Total Returns', 'Processed', 'Total e-file', 'Tax', 'Self-prepared', 'Visits', 'Number', 'Amount', 'Average', 'Num', 'Am', 'Avg']

# Clean up column names if necessary (remove leading/trailing spaces, etc.)
data.columns = data.columns.str.strip()

# Print the cleaned column names
#print(data.columns)

#print("Unique Years:", data['Year'].unique())

# Filter the data for the year 2023
if 'Year' in data.columns:
    returns_2023 = data[data['Year'] == '2023']
    #print("Filtered Data for 2023: ", returns_2023)

    #print(returns_2023['Processed'])

    # Remove commas and convert 'Total Returns' column to numeric
    returns_2023.loc[:,'Total Returns'] = returns_2023['Total Returns'].str.replace(',', '').astype(float)

    returns_2023.loc[:,'Processed'] = returns_2023['Processed'].str.replace(',', '').astype(float)

    total_sum = returns_2023['Total Returns'].sum() + returns_2023['Processed'].sum()
    returns_sum = returns_2023['Total Returns'].sum()

    number_of_entries_2023 = len(returns_2023)
    print(f"The number of income tax return entries in 2023 is: {number_of_entries_2023}")
    print(f"The total sum of 'Total Returns' and 'Processed' for the year 2023 is: {total_sum}")
    print(f"The total sum of 'Total Returns' for the year 2023 is: {returns_sum}")
else:
    print("The 'Year' column is not found in the data.")
