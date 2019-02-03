from selenium import webdriver

web = webdriver.Firefox(
    executable_path='/usr/local/bin/geckodriver',
    firefox_binary='/usr/lib/firefox-esr/firefox-esr'
)

web.get('https://www.youtube.com/')
