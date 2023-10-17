import requests
import pandas as pd
from bs4 import BeautifulSoup
import psycopg2  

# Define your PostgreSQL database connection parameters
db_params = {
    'dbname': 'Connect_Wiki',
    'user': 'postgres',
    'password': '****',
    'host': 'localhost',
    'port': '5432'
}

# Connects to the PostgreSQL database
connection = psycopg2.connect(**db_params)

url = 'https://en.wikipedia.org/wiki/List_of_largest_corporate_profits_and_losses'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Helps find the designated table that needs to be parsed
table = soup.find('table')

# Reads table, also used strip to clean up
table_titles = [th.text.strip() for th in table.find_all('th')]

# Create a DataFrame
df = pd.DataFrame(columns=table_titles)

# Create a cursor
cursor = connection.cursor()

# Iterate over the rows in the table
for row in table.find_all('tr'):
    # Find all the data cells in the current row
    row_data = row.find_all('td')
    # Get the text of cells in the current row
    row_values = [cell.text.strip() for cell in row_data]
    # Check if row has elements of columns
    if len(row_values) == len(table_titles):
        # Insert the data into the PostgreSQL database
        cursor.execute(
            "INSERT INTO your_table (column1, column2, ...) VALUES (%s, %s, ...)",
            tuple(row_values)
        )

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()
