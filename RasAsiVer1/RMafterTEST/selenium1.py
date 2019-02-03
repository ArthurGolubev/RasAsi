from selenium import webdriver

driver = webdriver.Firefox(firefox_profile=profile, log_path='./Log/geckodriver.log')

driver.get('https://24-ok.ru/')
