"""                        Le crawler                       """

                    ## Les bibliothéques
from pylab import *
from numpy import *
from scipy import fftpack
import requests
import pandas as pd
import time
import datetime
from bs4 import BeautifulSoup

                   ## Collecter du contenu du lien URL
url2="https://www.boursorama.com/cours/1rPSTLA/" #lien du site
page=requests.get(url2)
page

                  ## Affichage du contenu HTML du site
page.content

                  ## Utilisation beautifulsoup pour afficher
soup=BeautifulSoup(page.content,"html.parser")

                  ## Extraction de la valeur de bourse
soup.find_all('div',class_="c-faceplate__body")[0].find('span').text

                ## fonction pour l'extraction de la valeur de la bourse
def val():
    page=requests.get(url2)
    soup=BeautifulSoup(page.content,"html.parser")
    valeur=soup.find_all('div',class_="c-faceplate__body")[0].find('span').text
    return valeur 
                  ## Création du dataframe
tab=[]
for step in range(1,3): 
    time.sleep(5) #5 secondes d'attente
    tab.append({"t":step,"temps": pd.Timestamp.now(),"valeur" : (val()) })
df = pd.DataFrame(tab)

                 ## Modification du dataframe pour l'utilisation d'aprés
#Les infos sur la data
df.info()
df.dtypes
#convertir "valeur" en nombre
df['valeur'] = pd.to_numeric(df['valeur'],errors = 'ignore')
df['temps'] = pd.to_numeric(df['temps'],errors = 'ignore')
df['valeur'].mean()
print(df)

                   ## Enregistrer en  csv
df.to_csv('data', index=False,encoding='utf-8') #save en csv
                  ##Lecture dans la console
pd.read_csv('data') 
