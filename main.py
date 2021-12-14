# import library
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# getting cookies
# with open('exported-cookies.json') as f:
#   cookies = json.load(f)[0]
#   cookies['sameSite'] = 'Strict'
#   cookies['domain'] = '.drivetest.ca'
#   print(cookies)

# declare variable 
stage = "https://stage-thr-autonomy.site/"
gucci = True

# options = webdriver.ChromeOptions()
# options.add_argument("/Users/patrickluo/Library/Application Support/Google/Chrome")


# initialize
while gucci:
    with  webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
        # driver = webdriver.Chrome(executable_path="/Users/patrickluo/Documents/chromedriver", options=options)
        driver.get(stage)
        # driver.add_cookie(cookies)
        # new_cookies = driver.get_cookies()
        # print(new_cookies)

        javaScript = "document.getElementById('email')"
        print(driver.execute_script(javaScript))
        time.sleep(100)


# while True:
#     time.sleep(10)
#     print('yes')
#     driver.add_cookie()


