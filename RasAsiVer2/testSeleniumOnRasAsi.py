from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("-headless")
options.add_argument("-disable-gpu")

chrome = webdriver.Chrome(chrome_options=options, executable_path="/usr/lib/chromium-browser/chromedriver")
chrome.get("http://google.fr")

print("Titre de la page: {}".format(chrome.title))
chrome.save_screenshot('screenshot.png')
