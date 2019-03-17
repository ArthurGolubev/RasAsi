import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')
from selenium import webdriver

from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))
display.start()
browser = webdriver.Firefox(executable_path='/home/pi/RasAsi/RasAsiVer2/geckodriver')
browser.get('https://www.google.com/')