# from .pid_Info import prost3
# from .PrintHelp import help1
# from .electricity_monitoring import electricity_monitoringFunction


def listOfOrder():
    variable1 = 0
    while variable1 == 0:
        print('\n-|External_Packeg|-'
              '\nДоступные команды:\n1 - prost3\n2 - getpid ERDAS\n3 - PrintHelp\n0 - back to main')
        comand1 = input('\nВведите команжу:\t')

        # if comand1 == '1':
        #     prost3()
        #     input('...[press Enter]...')
        # elif comand1 == '2':
        #     getpid()
        # elif comand1 == '3':
        #     help1()
        # elif comand1 == '0':
        #     return 0
        # else:
        #     print('\nВы ввели не верную команду\nпопробуйте сново')
        #     input('...[press Enter]...')