
def ThrowError(ErrorMessage):

  print(f"\033[0m\033[31m'{ErrorMessage}")

def Pkg(cmdinput):

  import os
  import requests
  
  
  Parameters = cmdinput.split(" ")

  if len(Parameters) <= 1:
    ThrowError("Correct Usage : $ pkg <install or uninstall> <pastebinlink> <filename>")
  else:


    if len(Parameters) < 4 or len(Parameters) > 5:
    
      if len(Parameters) < 2:
        ThrowError("Correct Usage : $ pkg <install or uninstall> <pastebinlink> <filename>")
      else:  
          
        Filename = Parameters[2]
        Filename = os.path.join("Packages",Filename)

        if not Filename.endswith(".txt"): Filename += ".txt"
            
        if Parameters[1].lower() == "run":
          
          if len(Parameters) == 3:
  
       
            if not os.path.exists(Filename):
              ThrowError("That file doesn't exist nigga")
            else:
  
              with open(Filename) as f:
                contents = f.read()
                try:
                  exec(contents)
                except Exception as e:
                  ThrowError("This code isn't executable")

                  
          else:
              ThrowError("Correct Usage : $ pkg <run> <filename>")
  
        elif Parameters[1].lower() == "uninstall":
          if not os.path.exists(Filename):
            ThrowError("That file doesn't exist nigga")
          else:
            os.remove(Filename)
            print("File removed")
        else:  # They didnt write run or uninstall
          ThrowError("Correct Usage : $ pkg <install or uninstall> <pastebinlink> <filename>")
    else:
      Install = Parameters[1]
      PastebinLink = Parameters[2]
      Filename = Parameters[3]
      
      Filename = os.path.join("Packages",Filename)
      
      if not Filename.endswith(".txt"): Filename += ".txt"
      if Install.lower() == "install":

        try:
          Res = requests.get(PastebinLink)
  
          RawText = Res.text
          
          if not os.path.exists(Filename):
  
         

            f = open(Filename,"w")
            f.write(RawText)
            f.close()
            
            print("File saved")
            
          else:
  
            ThrowError("That file already exists nigga")

        except Exception as e:
          ThrowError("Invalid pastebin link")
      else:
        ThrowError("Correct Usage : $ pkg <install or uninstall> <pastebinlink> <filename>")





     
            
          
