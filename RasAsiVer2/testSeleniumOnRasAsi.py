import sys
sys.path.append('/home/pi/.local/lib/python3.5/site-packages/')
from selenium import webdriver

browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.google.com/')