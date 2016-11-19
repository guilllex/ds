#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

 
import os

import requests
import getpass
#import curses
import json
from prettytable import PrettyTable

actualPosition = 1
staticUrl = ""
nom = ""

msgMenuPosition = "Vous etes dans le menu "
msgGreeting = "Bounjour, "
msgMenuSelect = "Entrez votre choix: "
msgYourUrl = "Entrez l'url: "
msgYourUrlParam = "Entrez le paramètre :"

msgMauvaiseTouche = nom + " , vous avez appuyer sur une mauvaise touche!"

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

nom = raw_input("Entrez votre nom: ")
msgGreeting = msgGreeting + nom
print(msgGreeting)

while actualPosition >=1:
           
    t = PrettyTable(['1', '2', '3', 'q', 'Meteo'])
    t.add_row(['Serveurs', 'Donnes', 'Mongodb', 'Quiter', 'meteoSoleilDemain'])
    
    thisMsgMenuSelect = t
    
    print(thisMsgMenuSelect)
    
    myMenuSelect = raw_input(msgMenuSelect)
    
    os.system('clear')  # on linux / os x

    actualPosition = myMenuSelect

    msgActualPosition = (msgMenuPosition, actualPosition)
    
    
    # choisir le server
    # TODO un systeme de gestion des serveurs
    if actualPosition == "1":
        
        print(msgActualPosition)
    
        t = PrettyTable(['ID', 'Name', 'URL'])
        t.add_row(['1', 'local', '127.0.0.1'])
        t.add_row(['2', 'kubuntu dev server', 'http://192.168.1.116:88'])
        print (t)
        
        serverChoice = raw_input("Entrez le ID du serveur auquel vous voulez accéder: ")

        if serverChoice == "1":
        
            staticUrl = "127.0.0.1"
        
        elif serverChoice == "2":
        
            #url = 'http://192.168.1.116:88'
            #payload = '{\"name\":\"test\"}'
            #options = {}
            #options['headers'] = {}
            #options['headers']['Content-Type'] = 'application/json'
            #options['parameters'] = {}
            #options['parameters']['api_key'] = 'my_api_key'
            #result = platform.api.post(url, payload, options)
            #data = result.read()
            #print data
            #jsonData = bunchify(json.loads(data))
            
            staticUrl = "http://192.168.1.116:88/api/v2/joomla/_table/" + "ud3yg_users?fields=*&include_count=true&include_schema=true&" + "token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsInVzZXJfaWQiOjEsImVtYWlsIjoiZ3VpbGxhdW1ldHJlbXBlQGRldmVsc29sdXRpb24uY29tIiwiZm9yZXZlciI6ZmFsc2UsImlzcyI6Imh0dHA6XC9cLzE5Mi4xNjguMS4xMTY6ODhcL2FwaVwvdjJcL3N5c3RlbVwvYWRtaW5cL3Nlc3Npb24iLCJpYXQiOjE0Nzg4MjM5NDQsImV4cCI6MTQ3ODgyNzU0NCwibmJmIjoxNDc4ODIzOTQ0LCJqdGkiOiI1NzdkZmYwOTc5YzM1OWU2MzU1N2MzNWYzOTM3OGQ5YyJ9.81VVynN1926HRbHmH1377MXixuDRFKMZ3hajAoJt7iA"
            
            print (staticUrl)
        
        else:
        
            print("Mauvais choix")
        
        

    elif actualPosition == "2":

        print(msgActualPosition)
        url = 'http://192.168.1.116:88/api/v2/system/admin/session'
        headers = {'connection': 'keep-alive', 'Content-Type': 'application/json', 'Accept': 'application/json', 'X-DreamFactory-Api-Key': '36fda24fe5588fa4285ac6c6c2fdfbdb6b6bc9834699774c9bf777f706d05a88', 'duration': '10', 'session_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsInVzZXJfaWQiOjEsImVtYWlsIjoiZ3VpbGxhdW1ldHJlbXBlQGRldmVsc29sdXRpb24uY29tIiwiZm9yZXZlciI6ZmFsc2UsImlzcyI6Imh0dHA6XC9cLzE5Mi4xNjguMS4xMTY6ODhcL2FwaVwvdjJcL3N5c3RlbVwvYWRtaW5cL3Nlc3Npb24iLCJpYXQiOjE0Nzg4NDc2NTQsImV4cCI6MTQ3ODg1MTI1NCwibmJmIjoxNDc4ODQ3NjU0LCJqdGkiOiJhZTc3OTYyMjg1OWNmZWQyNTM0YTcyN2ZhNzk4ZTI3ZiJ9.VRBy34GFf3yGKZasKzAhL8pA_1Rbiq-OVGBadxz6B6M'}
        
        adminLoginEmail = raw_input("Entrez votre email admin: ")
        adminLoginPass = getpass.getpass("Entrez votre email admin: ")
        
        r = requests.get(url, headers=headers, auth=(adminLoginEmail, adminLoginPass))

        rStatusCode = r.status_code
        print(rStatusCode)
        rJson = r.json()
        # print rJson
        rText = r.text
        print(rText)
        
        rToken = rJson['session_token']
        rName = rJson['first_name']
        
        print("Bonjour " , rName, " Votre token est: ")
        print(rToken)
        
        # TEST fetch and print in a table start
        
        #url = raw_input(msgYourUrl)g
        #param= raw_input(msgYourUrlParam)
        fullurl = "http://192.168.1.116:88/api/v2/joomla/_table/ud3yg_users?fields=*&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEsInVzZXJfaWQiOjEsImVtYWlsIjoiZ3VpbGxhdW1ldHJlbXBlQGRldmVsc29sdXRpb24uY29tIiwiZm9yZXZlciI6ZmFsc2UsImlzcyI6Imh0dHA6XC9cLzE5Mi4xNjguMS4xMTY6ODhcL2FwaVwvdjJcL3N5c3RlbVwvYWRtaW5cL3Nlc3Npb24iLCJpYXQiOjE0Nzg4NDc2NTQsImV4cCI6MTQ3ODg1MTI1NCwibmJmIjoxNDc4ODQ3NjU0LCJqdGkiOiJhZTc3OTYyMjg1OWNmZWQyNTM0YTcyN2ZhNzk4ZTI3ZiJ9.VRBy34GFf3yGKZasKzAhL8pA_1Rbiq-OVGBadxz6B6M"

        resp = requests.get(url=fullurl)
        respJson = resp.json()
        
        
        
        for key, value in respJson.items():
            print(key, value)
        #print respJson['resource'][item]['name']
        #dbUserName = resp['resource'][0]['name']
        
        #from prettytable import PrettyTable
        #t = PrettyTable(['Name', 'Age'])
        #t.add_row(['dbUserName', 24])
        #t.add_row(['Bob', 19])
        #print t
        
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

