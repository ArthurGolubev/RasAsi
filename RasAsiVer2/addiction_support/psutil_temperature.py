import sys, psutil, time
from datetime import datetime
from RasAsiVer2.Google.GoogleGmail import GoogleGmail


class TemperatureSensor:
    temperature_55 = 0
    temperature_60 = 0
    temperature_65 = 0

    def temperature_sensor(self):
        if sys.platform == 'win32':
            return
        else:
            temp = []
            t = psutil.sensors_temperatures()
            for i in t['coretemp']:
                temp.append(i[1])
            t = max(temp)
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
                GoogleGmail().send_message(topic=f'Температура {t}♨🌡',
                                         message_text=f'Температура процессора {t} дата <br>{datetime.today()}')
            elif self.temperature_60 == 3:
                GoogleGmail().send_message(topic=f'Температура {t}♨🌡',
                                         message_text=f'Температура процессора {t} дата {datetime.today()}')
            elif self.temperature_65 == 1:
                GoogleGmail().send_message(topic=f'Температура {t}♨🌡',
                                         message_text=f'Температура процессора {t} дата {datetime.today()}')
                time.sleep(60)


if __name__ == '__main__':
    te = TemperatureSensor()
    te.temperature_sensor()
