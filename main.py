import requests

proxies={
    'http':'http://USERNAME:PASSWORD@pr.oxylabs.io:7777',
    'https':'https://USERNAME:PASSWORD@pr.oxylabs.io:7777',
}
response = requests.post('https://oxylabs.io/', proxies=proxies)
print(response.text)
