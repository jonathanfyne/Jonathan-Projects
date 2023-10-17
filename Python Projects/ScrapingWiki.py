import requests
import pandas as pd
from bs4 import BeautifulSoup

#can be tailored specifically, if I was given another url
url = 'https://en.wikipedia.org/wiki/List_of_largest_corporate_profits_and_losses'  
response = requests.get(url)

# Parsing the HTML content from wikipedia site using BeautifulSoup and response variable
soup = BeautifulSoup(response.content, 'html.parser')

# Helps find the designated table that needs to be parsed
table = soup.find('table')

# Reads table, also used strip to clean up
table_titles = [th.text.strip() for th in table.find_all('th')]

# Prints the table titles
#print('\t'.join(table_titles)) - just checking to see

#here is the actual dataframe
df = pd.DataFrame(columns = table_titles)

# Iterate over the rows in the table
for row in table.find_all('tr'):
    
    # Find all the data cells in the current row
    row_data = row.find_all('td')
    
    # Prints text of cell in the current row
    row_values = [cell.text.strip() for cell in row_data]
    
    # Checks if row has elements of columns 
    if len(row_values) == len(df.columns):
        df.loc[len(df)] = row_values

df 

