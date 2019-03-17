import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
from selenium import webdriver

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))
display.start()
browser = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.google.com/')