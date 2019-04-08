from selenium import webdriver
from time import sleep

tomorrow = 7
browser = webdriver.Firefox(executable_path=r'C:\PycharmProjects\RasAsi\RasAsiVer2\Weather_Packeg\geckodriver.exe')
browser.get('https://www.ventusky.com/')
browser.find_element_by_xpath(f"//div[@id='m']/a[@class='s t']").click()
browser.find_element_by_xpath(f"//table//tr//td//a[contains(text(), '{tomorrow}')]").click()