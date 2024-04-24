from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get('https://oxylabs.io/blog/')

blog_titles = driver.find_elements(By.CSS_SELECTOR, 'a.e10z4og6')
for title in blog_titles:
    print(title.text)
driver.quit() #closing the browser