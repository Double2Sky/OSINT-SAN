##!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os

# set color
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'

page_1 = '''{1}

  $$\                     $$\                        $$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\ $$$$$$$$\        $$$$$$\   $$$$$$\  $$\   $$\ 
  $$ |                    $$ |                      $$  __$$\ $$  __$$\ \_$$  _|$$$\  $$ |\__$$  __|      $$  __$$\ $$  __$$\ $$$\  $$ |
  $$ | $$$$$$\   $$$$$$\  $$ |  $$\  $$$$$$$\       $$ /  $$ |$$ /  \__|  $$ |  $$$$\ $$ |   $$ |         $$ /  \__|$$ /  $$ |$$$$\ $$ |
  $$ |$$  __$$\  \____$$\ $$ | $$  |$$  _____|      $$ |  $$ |\$$$$$$\    $$ |  $$ $$\$$ |   $$ |         \$$$$$$\  $$$$$$$$ |$$ $$\$$ |
  $$ |$$$$$$$$ | $$$$$$$ |$$$$$$  / \$$$$$$\        $$ |  $$ | \____$$\   $$ |  $$ \$$$$ |   $$ |          \____$$\ $$  __$$ |$$ \$$$$ |
  $$ |$$   ____|$$  __$$ |$$  _$$<   \____$$\       $$ |  $$ |$$\   $$ |  $$ |  $$ |\$$$ |   $$ |         $$\   $$ |$$ |  $$ |$$ |\$$$ |
  $$ |\$$$$$$$\ \$$$$$$$ |$$ | \$$\ $$$$$$$  |       $$$$$$  |\$$$$$$  |$$$$$$\ $$ | \$$ |   $$ |         \$$$$$$  |$$ |  $$ |$$ | \$$ |
  \__| \_______| \_______|\__|  \__|\_______/        \______/  \______/ \______|\__|  \__|   \__|          \______/ \__|  \__|\__|  \__|
          
  {0}Будет пополнятся по мере свободного времени.  
         
  Вся информация взята из общего доступа, вся ответственность лежит на вас если вы их загрузите. Мы только нашли ссылки на источник,
  пожалуйста проверяйте данные после загрузки с торрент на {1}virus total{0}. Мы проверить успели не все данные, загруженные с торрент.
 
  {0}Информация находится на редактировании. Ожидайте update 4.5
                                                                                                                              
  {0}[ {1}99{0} ] {2}Выйти...       {0}[ {1}0{0} ] {2} Загрузить данные об утечках.              
  
'''.format(GNSL, REDL, WHSL)


def leaks_menu():
    os.system("printf '\033]2;OSINT Утечки\a'")
    os.system('clear')

    print(page_1)
    option = input(f"{REDL}  └──>{ENDL} Введите 99 для выхода : {ENDL} ")
    
    while True:
        if option == '99':
            print()
            print("{1}  [{0} + {1}]{2} Спасибо за использование нашего Exploit.".format(REDL, GNSL, WHSL))
            return

        elif option == '0':
            print("{1}[ {0}+{1} ]{2} Загрузка с github...{3}".format(REDL, GNSL, WHSL, ENDL))
            return
        else:
            continue
