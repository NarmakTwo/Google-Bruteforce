import random
import glogin

def crack(id, settings, clear):
  clear()
  print('Cracking...')
  alphabet = ('a b c d e f g h i j k l m n o p q r s t u v w x y z ' + 'a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 ~ | : " \' ( ) - + ! @ # $ % ^ & * > < ? [ ] { } , . / \\ `'.upper()).split(' ')

  def go():
    g = ''
    for i in range(1, random.randint(1,settings['mLength'])):
      g += random.choice(alphabet)
    if g in guessed:
      g = go()
    return g

  global guess
  guess = ''
  global guessed
  guessed = []
  while not glogin.login(id,guess):
    guess = go()
  return guess, id
