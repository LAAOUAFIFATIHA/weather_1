from flask import Flask,render_template,request
from datetime import datetime
import requests
import json
import projet2


#------copy----------------------------------------------------------------------*

# app = Flask(__name__)

# @app.route("/traitement", methods=['POST'])
# def traitement():
#     if request.method == 'POST':
#         nom = request.form['ville']
#         name = "\'"+nom+"\'"
#         # Effectuez le traitement ici
#         return name
#     else:
#         return "Erreur : méthode non autorisée"
# nom_ville =traitement()

gpsdict= {"Essaouire":( "31,51", "-9,77"),
          "safi":("32,300815" , "-9,227203"),
           "ouajda":("34,0132500 ",  "-6,8325500"),
           "marakech":("31,630000" , "-8,008889"),
           "jagora":( "30,3324100" , "-5,8384000")}

#---get le nom  du ville 
#nom_ville = traitement()

# def ville(nom_ville,gpsdict):
#   res = gpsdict[nom_ville]
#   latitude = res [0]
#   longitude = res [1]
#   latitude = int(latitude)
#   longitude = int(longitude)
#   url="https://api.open-meteo.com/v1/forecast?latitude="+latitude+",&longitude="+longitude

#   return url
# cor_ville =ville(nom_ville , gpsdict)
# url = ville (nom_ville , gpsdict)



dateLyouma=datetime.today().strftime("%Y-%m-%d")
lyouma = dateLyouma
nomLyouma=datetime.today().strftime("%A")
jours={'Monday':'Lundi','Tuesday':'Mardi', 'Wednesday':'Mercredi',
'Thursday':'jeudi', 'Friday':'Vendredi', 'Saturday':'Samedi','Sunday':'dimanche'}
nhar= jours[nomLyouma]
maintenant = datetime.now()
#-------------------list des heurs----------------
heurs = ["0:00","3:00","9:00","12:00","15:00","18:00","21:00","24:00"]


url="https://api.open-meteo.com/v1/forecast?latitude="+projet2.latitude+",&longitude="+projet2.longitude
url=url+"&hourly=temperature_2m"
url=url+"&hourly=wind_speed_10m"
url=url+"&hourly=cloud_cover"
url=url+"&daily=sunrise"
url=url+"&daily=sunset"
url=url+"&hourly=rain"
url=url+"&start_date="+lyouma
url=url+"&end_date="+lyouma

response=requests.get(url)
response=requests.get(url).content.decode('utf-8')
data = json.loads(response)
#--------les  fonctions
def ri3valeur(listy):
  li=[]
  for i in range(0,len(listy),3):
    li.append(listy[i])
  return (li)


  #-----pour les valeur de metio

listrain = ri3valeur(data[0]["hourly"]["rain"])
listeTemp = ri3valeur(data[0]["hourly"]["temperature_2m"])
listwind = ri3valeur(data[0]["hourly"]["wind_speed_10m"])
listecloud = ri3valeur(data[0]["hourly"]["cloud_cover"])
windlist = data[0]["hourly"]["wind_speed_10m"]

listsunset = data["daily"]["sunset"]
listsunrise = data[0]["daily"]["sunrise"]
#-------------------new time---------------------------
from datetime import datetime
dateLyouma=datetime.today().strftime("%d-%m-%Y")
newlyouma = dateLyouma
#---------------function----pour---metre----les--images-----------------
heurs = ["00:00","03:00","09:00","12:00","15:00","18:00","21:00","24:00"]
dictTemp ={}
suns =int(listsunset[0][11:13])
sunr = int(listsunrise[0][11:13])
#--------------dict pour envoyer
listdict =[]
for i in range(8):
  dicttow={}
  dicttow["temperature"] =listeTemp[i]
  if i >= 4 :
    dicttow["temps"] = "{}:00".format(i*3)
  else:
    dicttow["temps"] = "0{}:00".format(i*3)
  dicttow["rain"] = listrain[i]
  dicttow["wind"] =str(max([windlist[0+i*3] ,windlist[1+i*3],windlist[2+i*3]]))+"-"+str(min([windlist[0+i*3] ,windlist[1+i*3],windlist[2+i*3]]))
  dicttow["cloud"] = listecloud[i]
  listdict.append(dicttow)
listdict


#---------------function----pour---metre----les--images-----------------
def getImagesSoliel (listeTemp,listecloud,listrain,listdict):
  for j,i  in enumerate(listeTemp) :
    heur =int(heurs[j][0:2])
    if i < 10 and listecloud[j] != 0 and listrain[j] == 0 :
      if sunr <= heur and suns >= heur:
        listdict[j]["image"]="images/sunCloudy.png"
      else :
        listdict[j]["image"]="images/moon_cloudy.png"

    elif  i < 10 and listrain[j] != 0 :
      if sunr <= heur and suns >= heur:
        listdict[j]["image"]="images/sunRain.png"
      else :
        listdict[j]["image"]="images/moon_rain.png"

    elif i < 20 and  listrain[j] != 0 :
      if sunr <= heur and suns >= heur and i < 20 :
          listdict[j]["image"]="images/sunRain.png"
      else:
        listdict[j]["image"]="images/moon_rain.png"
        
    elif i <20 and listecloud[j] != 0 and  listrain[j] == 0 :
      if sunr <= heur and suns >= heur and i <20:
         listdict[j]["image"]="images/sunCloudy.png"
      else :
       listdict[j]["image"]="images/moon_cloudy.png"
    elif i <20   :
      if sunr <= heur and suns >= heur and i <20:
         listdict[j]["image"]="images/1.png"
      else :
       listdict[j]["image"]="images/moon_cloudy.png"
    
    else :
      if sunr <= heur and suns >= heur  :
        listdict[j]["image"]="images/soliel_choud.png"
      else:
         listdict[j]["image"]="images/moon.png"

  return listdict 
listdict = getImagesSoliel(listeTemp,listecloud,listrain,listdict)

ph ="images/soliel_choud.png"








      


