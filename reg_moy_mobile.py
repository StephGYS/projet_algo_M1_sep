"""                     La moyenne mobile                      """
## La Moyenne mobile est fréquemment utilisée pour étudier les données 
#de séries chronologiques en calculant la moyenne des données à des 
#intervalles spécifiques.
##Objectif: on cherche le graphe colle le plus au nuage de points

                     ##Les bibliothéques
from pylab import *
from numpy import *
from scipy import fftpack
import requests
import pandas as pd
import time
import datetime
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from sklearn.metrics import *

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures

                      ## Importation de la data
df= pd.read_csv('stellantis')

                      ##Visualisation
df.plot.line(x='temps',y='valeur',marker='+')
plt.title('Evolution de Stellantis en environ 17 minutes')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.legend()

                ## Calcul de la moyenne mobile 
df['Moving Average']=df['valeur'].rolling(window=1).mean()
#On fait varier 'window' pour avoir un graphe qui colle le mieux 
#au graphe des valeurs
#REMARQUE: la moyenne mobile  s'ajoute directement dans le dataframe

                ## Visualisation de la moyenne mobile
df.plot.line(x='temps',y='Moving Average')
df.plot.line(x='temps',y=['valeur','Moving Average'])
plt.title('Evolution de Stellantis avec la moyenne mobile sur 1 jour')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.legend()

             ## Calcul de la moyenne mobile centré 
df['Rolling Average Center']=df['valeur'].rolling(window=5, center=True).mean()
             ## Visualisation  la moyenne mobile centré
df.plot.line(x='temps',y=['valeur','Rolling Average Center'])
plt.title('Evolution de Stellantis avec la moyenne mobile centrée')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.legend()

            ## Enregister la nouvelle data sous un notre nom
df.to_csv('stellantis_new', index=False,encoding='utf-8')
Stellantis=pd.read_csv('stellantis_new')

            ## Evaluation du modele  
#Calcul brute du MAE
erreur_predict=abs(mean(Stellantis['valeur']-Stellantis['Moving Average']))
print(erreur_predict)

# Calcul du MAE 
print('MAE:', mean_absolute_error(Stellantis['valeur'],Stellantis['Moving Average']))

# Calcul du MSE
print('MSE:', sqrt(mean_squared_error(Stellantis['valeur'],Stellantis['Moving Average'])))
     #L'erreur entre y et y_pred est n'est pas tres grande

# Median absolute error (Erreur médian)
print('median abs err:', median_absolute_error(Stellantis['valeur'],Stellantis['Moving Average']))
     #l'erreur de prediction est d'environ 1.4210854715202004e-14

           ## L'histogramme des erreurs
err_hist= abs(Stellantis['valeur']-Stellantis['Moving Average'])
plt.hist(err_hist)
plt.title('Histogramme des erreurs predits')
plt.xlabel('erreur')
plt.ylabel('pourcentage')
plt.legend()
     #50% des valeurs predit ont une erreur proche de 0.5

           ## Calcul de R^2
r2=r2_score(Stellantis['valeur'],Stellantis['Moving Average'])
print(r2)
     #Ce modele decrit 100% des variations des  valeurs de stellantis