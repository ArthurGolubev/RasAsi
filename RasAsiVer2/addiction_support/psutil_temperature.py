import sys, psutil, time
from RasAsiVer2.Google.GoogleGmail import GoogleGmail


class TemperatureSensor:
    test_temperature = 0
    temperature_55 = 0
    temperature_60 = 0
    temperature_65 = 0

    def temperature_sensor(self):
        if sys.platform == 'win32':
            return
        else:
            t = psutil.sensors_temperatures()
            if 50 <= t < 55:
                self.test_temperature += 1
                print('test - ', t)
            else:
                self.test_temperature = 0

            if 55 <= t < 60:
                self.temperature_55 += 1
            else:
                self.temperature_55 = 0

            if 60 <= t < 65:
                self.temperature_60 += 1
            else:
                self.temperature_60 = 0

            if 65 <= t:
                self.temperature_65 += 1
            else:
                self.temperature_65 = 0

            if self.temperature_55 == 5:
                GoogleGmail.send_message(topic='Температура ♨🌡',
                                         message_text=f'Температура процессора {t}')
            elif self.temperature_60 == 3:
                GoogleGmail.send_message(topic='Температура ♨🌡',
                                         message_text=f'Температура процессора {t}')
            elif self.temperature_65 == 1:
                GoogleGmail.send_message(topic='Температура ♨🌡',
                                         message_text=f'Температура процессора {t}')
                time.sleep(60)
            elif self.test_temperature == 11:
                GoogleGmail.send_message(topic='Температура ♨🌡',
                                         message_text=f'Температура процессора {t}')

if __name__ == '__main__':
    te = TemperatureSensor()
    te.temperature_sensor()
