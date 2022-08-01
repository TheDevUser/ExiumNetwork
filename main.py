import boot.reg.system_cli.graphics as graphics
import getpass
import os
import requests
import boot.reg.system_func.functions as functions 

useros = str(os.name).capitalize()

print(f"{useros} Detected")


if useros == 'Windows':
  clr = lambda: os.system('cls')
elif useros == 'Linux':
  clr = lambda: os.system('clear')
elif useros == 'Darwin':
  clr = lambda: os.system('clear')
elif useros == "Posix":
  clr = lambda: os.system('clear')
else:
  clr = lambda: os.system('clear')



helplist = requests.get("https://pastebin.com/raw/Z4G5MXbc")

print(graphics.loading)

combolist = open('combolist.txt').read().splitlines()

choice = input('login or register: ')

#login

auth = False

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
  clr()
  print(graphics.copyright)
  while True:
    cmdinput =input("\033[32muser@exiumnetwork\033[0m:\033[36m∼\033[0m$ ")

    if cmdinput == "help":
      print()
      print(helplist.text)
      print()
    elif cmdinput == "useless":
      print("\nwhat did u think this would do\n")
    elif cmdinput == "clear":
      clr()
      print(graphics.copyright)
    elif cmdinput == "neofetch":
      print(graphics.neofetchgraph)
    elif cmdinput.startswith("app"):

      functions.Pkg(cmdinput)
      
    elif cmdinput == "terminal":
      exec(open("./user/apps/terminal/terminal.py").read())
    elif cmdinput == "credits":
      print("Ezreali - Everything")
    else:

      if cmdinput.strip() != "":
        print("\n\033[31m" + "'\033[4m" + cmdinput + "\033[0m\033[31m'" + " is an invalid command! Type 'help'' for a list of commands.\n")