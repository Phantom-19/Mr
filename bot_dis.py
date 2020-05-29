#Désolé, vous ne pouvez pas exécuter ce script dans Dcoder :)
# exécuter ce script en dehors de l'application dcoder
# ° Utilisateur Android °
# • Vous pouvez l'exécuter dans le termux sur lequel Python est installé et le package de bibliothèque discord.py
# • pip install discord.py

# Pour plus d'informations
# documentation: https://discordpy.readthedocs.io/en/latest/

# Je modifie ceci pour donner une note Ce robot de discordance Python ne peut pas fonctionner sur Dcoder

"""
Q: Où puis-je obtenir un jeton?
R: Vous pouvez obtenir un jeton depuis https://discordapp.com/developers/, connectez-vous à votre compte discord et suivez l'étape

Q: comment exécuter Bot sans que mon ordinateur soit toujours en ligne
A: Exécuter sur VPS, par exemple Heroku, Vultr, AWS
R: Cela fera fonctionner le bot 24h / 24 et 7j / 7 sans que votre ordinateur soit toujours allumé et en ligne, sauf si vous fermez le bot

"""
#Package

import sys
try:
  import discord
  from discord.ext import commands
  from discord.ext.commands import Bot
except:
  print("[!] discord.py  n\'est pas installer")
  print("[i] Désolé ce robot ne peut être exécuter sur  Dcoder")
  sys.exit()
#Config
token = "<Votre jeton>" # entrer votre  jeton
prefix = "<Votre prefixe>" # 

gamestatus = "Robot priver de Faxel " # 

client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
  print("Discord Package Version" + discord.__version__)
# Changement de Status sur  discord  

  await client.change_presence(status=discord.Status.online,activity=discord.Game(gamestatus))
  print("Discord robotiser de   Faxel")
  print('Bonjour ici! Entré comme {0.user}'.format(client))
  print("Connexion au  robot de Faxel !")


# COMMENT FAIRE RÉPONDRE VOTRE ROBOT
# <votre préfixe> <commande>
# exemple:> bonjour
# ">" est votre préfixe
# "bonjour" est votre commande

# Ok ici nous allons faire répondre le  robot au message

# ENVOYER UN MESSAGE BONJOUR

@client.command()
async def hello(ctx):
  await ctx.send(f"Hello ^_^ {ctx.author.mention}")
  
# ↓ Vous pouvez ajouter plus de commandes ici ↓






  
  # RENDRE CE SCRIPT CONNECTÉ AU ROBOT

client.run(token)