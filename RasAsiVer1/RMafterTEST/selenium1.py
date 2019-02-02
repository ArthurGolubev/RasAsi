from selenium import webdriver

driver = webdriver.Firefox(firefox_profile=profile, log_path='./Log/geckodriver.log')

browser.get('https://24-ok.ru/')
