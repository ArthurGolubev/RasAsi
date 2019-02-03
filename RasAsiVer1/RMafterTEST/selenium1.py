from selenium import webdriver

web = webdriver.Firefox(
    executable_path='/path/to/geckodriver',
    firefox_binary='/path/to/firefox/binary'
)

browser.get('https://www.youtube.com/')
