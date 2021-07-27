import yaml
import os

os.popen('color F0')
try:
      with open('C:/AutoCmd/commands.yaml', 'r') as file:
            commands = yaml.load(file, Loader=yaml.FullLoader)
            commands = commands[0]['commands']
            if commands == None:
                  del commands
                  commands = []

except:
      with open('C:/AutoCmd/commands.yaml', 'w') as file:
            yaml.dump([{'commands': []}], file)

      with open('C:/AutoCmd/commands.yaml', 'r') as file:
            commands = yaml.load(file, Loader=yaml.FullLoader)
            commands = commands[0]['commands']
            if commands == None:
                  del commands
                  commands = []

running = True
while running:
      print()
      print("===================================================")
      print("[1] See registered commands")
      print("[2] Register command")
      print("[3] Delete command")
      print("[4] Save and exit")
      print("===================================================")

      mode = input('>> ').split()[0]

      if mode == "1":
            print()
            print("*************************************************")     
            for cmd in commands:
                  print(f"      -- {cmd}")
            print("*************************************************")

      elif mode == "2":
            print("Please enter the command bellow:")
            commands.append(input("      >>> "))
            print(commands)
            with open('C:/AutoCmd/commands.yaml', 'w') as file:
                  yaml.dump([{'commands': commands}], file)

      elif mode == "3":
            print("Please enter the command to delete:")
            with open('C:/AutoCmd/commands.yaml', 'w') as file:
                  remove = input("      >>> ")
                  commands.remove(remove)
                  yaml.dump([{'commands': commands}], file)
      elif mode == "4":
            print("***********")
            print("Exiting")
            print("***********")
            running = False
      
      



