import sys
from selenium import webdriver

browser = webdriver.Firefox(executable_path='/home/pi/RasAsi/RasAsiVer2/geckodriver')
browser.get('https://www.google.com/')