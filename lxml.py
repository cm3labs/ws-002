import requests
from lxml import html

url = 'https://oxylabs.io/blog/products'
response = requests.get(url)

tree = html.fromstring(response.text)

blog_titles = tree.xpath('//a[contains(@class, "e10z4og6")]')
for title in blog_titles:
    print(title.text)

# NOTE: I was not able to get lxml going. I need more practice on this, or reflection on if I want this to work at all.
    
# /tutorial/ws-002$  cd /home/user/projects/python/tutorial/ws-002 ; /usr/bin/env /home/user/projects/python/tutorial/ws-002/venv/bin/python /home/user/.vscode/extensions/ms-python.debugpy-2024.2.0-linux-x64/bundled/libs/debugpy/adapter/../../debugpy/launcher 37111 -- /home/user/projects/python/tutorial/ws-002/lxml.py 
# Traceback (most recent call last):
#   File "/home/user/projects/python/tutorial/ws-002/lxml.py", line 2, in <module>
#     from lxml import html
#   File "/home/user/projects/python/tutorial/ws-002/lxml.py", line 2, in <module>
#     from lxml import html
# ImportError: cannot import name 'html' from partially initialized module 'lxml' (most likely due to a circular import) (/home/user/projects/python/tutorial/ws-002/lxml.py)