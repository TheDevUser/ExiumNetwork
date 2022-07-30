import graphics as graphics
import commands as cmd
import getpass
import os
import requests

print(graphics.loading)

combolist = open('combolist.txt').read().splitlines()

clear = lambda: os.system('clear')

choice = input('login or register: ')

#login
if choice == 'login':
    print('Please enter a username and password')
    user = input('Username: ')
    passw = getpass.getpass('Password: ')

    combo = user + ':' + passw

    if combo in combolist:
        print('Logged in with the username:', user)
        auth = True
    else:
        print('Does not exist or wrong username and password')
        auth = False

      
 # register
if choice == 'register':
    username_valid = True
    print('Enter the desired username')
    wanted_user = input('Username: ')
    for combo in combolist:
      if wanted_user in combo:
        print('Username is taken! Make another!')
        username_valid = False
    if username_valid == True:
      wanted_pass = getpass.getpass('Password: ')
      wanted_passw = getpass.getpass('Confirm Password: ')
      if wanted_pass != wanted_passw:
        print('Passwords do not match')

      combo = wanted_user + ':' + wanted_pass

      f1 = open('combolist.txt', 'a+')
      f1.writable()
      f1.write(combo + '\n')
      f1.close()

      print('Successfully registered! Try and login.')
      user = wanted_user
      auth = True

if auth:
  clear()
  print(graphics.copyright)
  while True:
    cmdinput =       input("\033[32muser@exiumnetwork\033[0m:\033[36m∼\033[0m$ ")

    if cmdinput == "help":
      print("\nno help for you L\n")
    elif cmdinput == "useless":
      print("\nwhat did u think this would do\n")
    elif cmdinput == "clear":
      clear()
      print(graphics.copyright)
    elif cmdinput == "neofetch":
      print(graphics.neofetchgraph)
    elif cmdinput == "pkg install":
      input1 = ("")
      r = requests.get("https://pastebin.com/raw/BChufCXg")
      pkgfile = open("mypackage.py", "x")
      pkgfile.write(r.text)
      pkgfile.close()
    elif cmdinput == "run":
      exec(open("./mypackage.py").read())
    else:
      print("\n\033[31m" + "'\033[4m" + cmdinput + "\033[0m\033[31m'" + " is an invalid command! Type 'help'' for a list of commands.\n")