import crack
import sys
from datetime import date
from os import name, system

def clear():
  if name == 'nt':
    system('cls')

  else:
    system('clear')


aSettings = {
  "mLength":int(sys.argv[2])
}

pwd, id = crack.crack(sys.argv[1], aSettings, clear)

with open('passwords.csv','a') as f:
    f.write(f'\n{date.today().strftime("%d/%m/%Y")}, {id}, {pwd}')
