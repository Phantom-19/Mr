#python 2.7.15

from time import sleep
import os, sys,time
raw_input= input 


 #-Automatisation-#
def Street(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.09)

Street("""\033[1;91m[\033[1;93m**\033[1;91m]\033[38;5;214m     Dev : Faxel        \033[1;91m[\033[1;93m**\033[1;91m] """)
  
print("")
Street ("\033[38;5;224m Generateur de  lien  pour la discussion sur whatsapp")
print("")    
numero = raw_input("\033[38;5;248mEntrer votre numero whatsapp \033[1;91m:\033[1;96m  ")

whatsapp_web =("https://whatsapp.com/")
whatsapp_api =("https://api.whatsapp.com/send?phone=")

#generateeur

if not numero:
  print("\033[1;91m")
  print ("Veuillez saisir un numéro whatsapp!")
else:
  print("\033[1;93m")
  print ("Procès en cours , patientez ...")
  time.sleep(4)
  print("\033[1;97m")
  print ("Votre lien de discussion whatsapp est\n\n\033[1;92m",whatsapp_api+numero)
  print("")
  Street ("\033[1;91m[\033[1;93m**\033[1;91m] \033[38;5;214mFaxel\033[1;97m un jour, \033[38;5;214mFaxel \033[1;97mtoujours    \033[1;91m[\033[1;93m**\033[1;91m]")
  print("\033[1;92m")
  print("\033[1;95m")
  