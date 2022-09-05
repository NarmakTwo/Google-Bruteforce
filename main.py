import sys
from time import sleep
from os import system, name
import crack
from datetime import date
from text import stext

def clear():
  if name == 'nt':
    system('cls')

  else:
    system('clear')

def write(text):
  for char in text:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
  sleep(0.2)
  print()


def start():
  clear()
  write('Welcome To...............')
  print(stext(1))
  sleep(0.3)
  print(stext(2))

  write('How may I help you today?')
  sleep(0.5)
  main_loop()


global aSettings
aSettings = {
  "mLength":25
}

def main_loop():
  print('1. Crack')
  sleep(0.15)
  print('2. Settings (Beta)')
  sleep(0.15)
  print('3. Exit')
  sleep(0.15)
  choice = input('>  ')
  if not choice.isdigit():
    print('Not a choice, try again')
    sleep(0.15)
    clear()
    main_loop()
  elif choice == '1':
    clear()
    pwd, id = crack.crack(aSettings, clear)
    clear()
    print(f'Lets Gooooooooooooo!!!!!!\n The password is {pwd}')
    with open('passwords.csv','a') as f:
      f.write(f'\n{date.today().strftime("%d/%m/%Y")}, {id}, {pwd}')
      
  elif choice == '2':
    settings()
    sleep(2)
    clear()
    main_loop()
  elif choice == '3':
    pass



def _settings():
  length = input('Maximum Length: ')
  if length.isdigit():
    aSettings['mLength'] = int(length)
  else:
    print('Maximum Length not a digit, try again')
    sleep(0.5)
    clear()
    _settings()

def settings():
  clear()
  _settings()  
  sleep(0.2)
  
  



if __name__ == '__main__':
  start()