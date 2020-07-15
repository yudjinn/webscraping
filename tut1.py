from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pathlib
import time

#Path to chrome driver (should be in project directory)
DRIVER_PATH = str(pathlib.Path().absolute()) + '/chromedriver'
driver = webdriver.Chrome(DRIVER_PATH)

driver.get('http://techwithtim.net')

search = driver.find_element_by_name('s')
search.send_keys('test')
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)

finally:
    driver.quit()
