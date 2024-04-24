import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://sandbox.oxylabs.io/products')

# what we find goes in results
results = []

# add page source to the variable 'content'
content = driver.page_source

# parse with beautiful soup
soup = BeautifulSoup(content, 'html.parser')

# Loop over al elements returned by the 'findAll' call.

for element in soup.findAll(attrs={'class': 'product-card'}):
    name = element.find('h4')
    if name not in results:
        results.append(name.text)

# quick test
# for x in results:
#     print(x)


# export to csv using pandas
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')