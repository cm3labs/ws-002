import requests
from bs4 import BeautifulSoup

url = 'https://oxylabs.io/blog/products'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# blog_titles = soup.find_all('a', class_='css-mkiwgq')
# for title in blog_titles:
#     print(title.text)

# import re

# blog_titles = soup.find_all('a', class_=re.compile('css-mkiwgq'))
# for title in blog_titles:
#     print(title.text)

blog_titles = soup.select('a.e10z4og6')
for title in blog_titles:
    print(title.text)