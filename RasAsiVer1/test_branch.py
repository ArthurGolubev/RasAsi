from selenium import webdriver

browser = webdriver.Firefox(executable_path='C:\PycharmProjects\RasAsi\credentials\geckodriver.exe')

browser.get('https://www.ventusky.com/?p=56.0;98.8;5&l=temperature-2m')
browser.find_element_by_xpath('//div[@class="qj l hv"]/div[@class="xx"]/select/option[@value="off"]').click()