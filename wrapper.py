print("Wrapper has started.")
import subprocess, time
from subprocess import CREATE_NEW_CONSOLE

check_seconds = 1 #The delay in seconds to check if process has died
debug = False #True/False Debug output
print("Creating Processes.")
lithia_process = subprocess.Popen(["python", "lithia.py"], shell=True)
print("Done.")

while True:
  lithia_poll = lithia_process.poll()
  if lithia_poll == None:
    if debug == True: 
      print(str(lithia_process) + " Is Still Alive")
    time.sleep(check_seconds)
  else:
    print(str(lithia_process) + " Has Died, rebooting process")
    lithia_process = subprocess.Popen(["python", "lithia.py"], shell=True)
