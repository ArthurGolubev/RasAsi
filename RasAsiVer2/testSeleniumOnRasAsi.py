from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/pi/RasAsi/RasAsiVer2/geckodriver', capabilities={"marionette": False})
browser.get('https://www.google.ru/')
