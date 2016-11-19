#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
import thread
import time
import requests
import getpass
import json
from prettytable import PrettyTable
from docker import Client
#cli = Client(base_url='unix://var/run/docker.sock')

actualPosition = 1
staticUrl = ""
name = ""

msgMenuPosition = "Vous etes dans le menu "
msgGreeting = "Bounjour, "
msgMenuSelect = "Entrez votre choix: "
msgYourUrl = "Entrez l'url: "
msgYourUrlParam = "Entrez le paramètre :"

msgMauvaiseTouche = name + " , vous avez appuyer sur une mauvaise touche!"

# meteo start

import pyowm

owm = pyowm.OWM('2234535667d73d1d333b5b2c0b9dd7d6')  # You MUST provide a valid API key

observation = owm.weather_at_place('Montreal,ca')
w = observation.get_weather()

wW = w.get_wind()
wH = w.get_humidity()
wT = w.get_temperature()

forecast = owm.daily_forecast("Montreal,ca")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)

if  forecast == True:

    meteoSoleilDemain = "Demain: Ensoleillé"
else:

    meteoSoleilDemain = "Demain: Nuageux"
    
# meteo stop

os.system('clear')  # on linux / os x

# splash screen start

print('\x1b[1;32;40m' + '8888b.   dP\"Yb   dP\"\"b8 88  dP 88 88b 88  dP\"\"b8' + '\x1b[0m')
print('\x1b[1;32;40m' + ' 8I  Yb dP   Yb dP   `\" 88odP  88 88Yb88 dP   `\"' + '\x1b[0m')
print('\x1b[1;32;40m' + ' 8I  dY Yb   dP Yb      88\"Yb  88 88 Y88 Yb  \"88' + '\x1b[0m')
print('\x1b[1;32;40m' + '8888Y\"   YbodP   YboodP 88  Yb 88 88  Y8  YboodP' + '\x1b[0m')
print(" ")
print('\x1b[1;32;40m' + '.dP\"Y8 888888    db    888888 88  dP\"Yb  88b 88' + '\x1b[0m')
print('\x1b[1;32;40m' + '`Ybo.\"   88     dPYb     88   88 dP   Yb 88Yb88 ' + '\x1b[0m')
print('\x1b[1;32;40m' + 'o.`Y8b   88    dP__Yb    88   88 Yb   dP 88 Y88 ' + '\x1b[0m')
print('\x1b[1;32;40m' + '8bodP\'   88   dP\"\"\"\"Yb   88   88  YbodP  88  Y8 ' + '\x1b[0m')
print(" ")

# splash screen start

time.sleep(2)

name = raw_input("Enter your name: ")
os.system('clear')  # on linux / os x
msgGreeting = msgGreeting + name
print('\x1b[1;32;40m' + 'Doking Station' + '\x1b[0m')
print(" ")
print(msgGreeting)

while actualPosition >=1:
           
    t = PrettyTable(['1', '2', '3', '4', '5'])
    t.add_row(['Docker', 'Monitor', 'Manage', 'Configuration', 'Quit'])
    
    thisMsgMenuSelect = t
    
    print(thisMsgMenuSelect)
    
    myMenuSelect = raw_input(msgMenuSelect)
    
    os.system('clear')  # on linux / os x

    actualPosition = myMenuSelect

    msgActualPosition = (msgMenuPosition, actualPosition)
    
    # TODO here we have to manage Docker container details from a mongodb so we can create, edit and delete Docker container details entry
    if actualPosition == "1":
        
        print(msgActualPosition)
        # TODO fetch real entry from mongodb
        t = PrettyTable(['ID', 'Name', 'port'])
        t.add_row(['1', 'python', '88:88'])
        t.add_row(['2', 'owncloud', '80:80'])
        print (t)
        # TODO fetch real entry from mongodb
        serverChoice = raw_input("Witch Docker ID you want to modify?: ")

        if serverChoice == t[1]:
        
            print("What do you want modify")
            print(" ")
            print("1 - ID")
            print("2 - Name")
            print("3 - Port")
        
        elif serverChoice == "2":
        
            print("What do you want modify")
            print(" ")
            print("1 - ID")
            print("2 - Name")
            print("3 - Port")
        
        else:
        
            print("Wrong choice!")
        
        

    elif actualPosition == "2":

        print(msgActualPosition)

        def input_thread(L):
            raw_input()
            L.append(None)
            
        def do_print():
            L = []
            thread.start_new_thread(input_thread, (L,))
            while 1:
                time.sleep(.1)
                if L: break
                t = PrettyTable(['Name', 'Port', 'CPU', 'Memory', 'Network'])
                t.add_row(['Webmin', '1000:1000', '15%', '257M', 'd:205K/u:534k'])
                print (t)
                
                
                cli = Client(base_url='tcp://127.0.0.1:2375')
                cli.containers()
                
                
                print("Press <ENTER> to stop and return to the menu")
                time.sleep(2)
                os.system('clear')  # on linux / os x
        do_print()
        
        # TEST fetch and print in a table end

        

    elif actualPosition == "3":

        print(msgActualPosition)
        
        

        import pymongo
        db_connect = pymongo.MongoClient('127.0.0.1', 27017)
        database_name = 'pyson'
        database = db_connect[database_name]
        collection = database.collection_names(include_system_collections=False)
        for collect in collection:
            print (collect)
        
        actualPosition = 1
        
    elif actualPosition == "q":

        byebye = raw_input("Voulez-vous vraiment quiter? o=oui n=non: ")

        if byebye == "o":

            actualPosition = 0
            
        else:
            
            actualPosition = 1
            
    else:

        print(msgMauvaiseTouche)
        
        

print("Byebye!")

