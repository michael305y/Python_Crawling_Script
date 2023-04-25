### using the webbrowswer library
# import webbrowser

# search_query = "KRA"
# url = "https://www.google.com/search?q=" + search_query
# webbrowser.open(url)

### using selenium to automate the web

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#####

###
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Create a Service object
service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Pass in the Service object to the webdriver.Chrome method
driver = webdriver.Chrome(service=service)


PATH = "C:\Program Files (x86)\chromedriver.exe"

# create a new Chrome browser instance
# driver = webdriver.Chrome(PATH)

# navigate to Google
# driver.get("https://www.google.com")
# driver.get("http://nemis.education.go.ke/")
driver.get("https://michael305.netlify.app")


while True:
    time.sleep(1)
# find the search box element and enter a query
# # search_box = driver.find_element_by_name("q")
# search_box = driver.find_element("q")
# search_box.send_keys("http://nemis.education.go.ke/")
# search_box.send_keys(Keys.RETURN)

# # wait for the search results to load
# driver.implicitly_wait(10)

# # find the first search result and click on it
# search_result = driver.find_element_by_css_selector("#search .g:first-of-type a")
# search_result.click()

# # close the browser
# driver.quit()
