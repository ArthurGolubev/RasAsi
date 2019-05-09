from time import sleep
from sys import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RasAsiVer2.Google.GoogleGmail import GoogleGmail
from RasAsiVer2.Decorators.Decorators import logging_decorator
from RasAsiVer2.Google.GoogleSpreadsheets import GoogleSpreadsheet


class TransportCard:

    def __init__(self, who):
        if who == 'me':
            self.number = GoogleSpreadsheet().get_spreadsheets_values(
                spreadsheet_id='1vqDWkRh8ERwxkRtyum-0bffbmjp7KMJn-SpAgNnYtyM',
                range_name='Лист1').get('values')[0][0]
            self.to = 'zabavniy7@gmail.com'
        elif who == 2:
            self.number = GoogleSpreadsheet().get_spreadsheets_values(
                spreadsheet_id='1vqDWkRh8ERwxkRtyum-0bffbmjp7KMJn-SpAgNnYtyM',
                range_name='Лист1').get('values')[0][1]

    @logging_decorator
    def transport_card(self):
        if platform == 'win32':
            executable_path = r'C:\PycharmProjects\RasAsi\credentials\geckodriver.exe'  # Laptop
            # executable_path = r'C:\PythonProject\RasAsi\credentials\geckodriver.exe'  # PC
        elif platform == 'linux':
            executable_path = r'/home/rasasi/RasAsi/credentials/geckodriver'  # Ubuntu Mate
        else:
            print(f'Платформа {platform} не поддерживается')
            return 0

        _options_webdriver = webdriver.FirefoxOptions()
        _options_webdriver.set_preference("intl.accept_languages", "ru")

        browser = webdriver.Firefox(executable_path=executable_path, options=_options_webdriver)
        browser.implicitly_wait(220)

        browser.get('https://www.krasinform.ru/')
        browser.find_element_by_xpath("//input[@type='text'][@name='card_num']").send_keys(f'{self.number}')
        sleep(5)
        browser.find_element_by_xpath("//input[@type='text'][@name='card_num']").send_keys(Keys.ENTER)
        sleep(5)
        transport_unit = browser.find_elements_by_xpath("//table[@class='table']//td")
        transport_unit = int(transport_unit[1].text.split(' ')[0])
        browser.close()

        GoogleGmail().send_message(to=self.to,
                                   topic='Проездной 🧐🚌💰',
                                   message_text=f'Оставшийся баланс на транспортной карте: {transport_unit} руб.')

if __name__ == '__main__':
    TransportCard(who='me').transport_card()
else:
    print(f'Подключен модуль {__name__}')