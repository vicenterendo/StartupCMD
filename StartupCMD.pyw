import yaml
import os

try: 
      with open('C:/AutoCmd/commands.yaml', 'r') as file:
            startcommands = yaml.load(file, Loader=yaml.FullLoader)
            startcommands = startcommands[0]['commands']
            if startcommands == None:
                  startcommands = []
      
      for cmd in startcommands:
            try:
                  os.system(cmd)
            except:
                  pass
except:
      pass
      
            