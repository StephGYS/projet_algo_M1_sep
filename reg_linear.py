"""                     Regression_lineaire                      """
# Objectif: on cherche la droite qui colle le plus au nuage de points
#  afin de faire  des prédictions futur.

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
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

                  ## Importation de la data
data= pd.read_csv('stellantis')
y=data.iloc[:,-1].values #val
x=data.iloc[:,1].values # temps
t=data.iloc[:,:-2].values  #pas

                  ## Le nuage de points
plt.scatter(t, y, color="red",marker = '+',label='')
plt.title('Evolution de Stellantis en environ 17 minutes')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.legend()
plt.show()

                ## Division du dataset en training et le test 
# Mon jeu de modele d'apprentissage est 1/3 du dataset
x_app,x_test,y_app,y_test= train_test_split(t, y,test_size = 1.0/3)

                ## Construstion du modele 
regressor= LinearRegression()
regressor.fit(x_app, y_app)

               ## Definir la prediction 
y_pred=regressor.predict(x_app)
y_predd=regressor.predict(t)

              ## Visualisation des resultats 
plt.scatter(x_app, y_app, color="red",marker = '+',label='')
plt.plot(x_app,y_pred,color="blue",label='droite de régression') 
plt.title('Evolution de Stellantis')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.legend()
plt.show

               ## Faire les predictions futur 
x_futur=x_test

              ## Evaluation du modele  
# Calcul brute du MAE
erreur_predict=mean(abs(y_test-regressor.predict(x_test)))
print(erreur_predict)

# Calcul du MAE
print('MAE:', mean_absolute_error(y,y_predd))

# Calcul du MSE 
print('MSE:', sqrt(mean_squared_error(y,y_predd)))
   #L'erreur entre y et y_pred est n'est pas tres grande 

# Median absolute error (Erreur médian)
print('median abs err:', median_absolute_error(y,y_predd))
    #l'erreur de prediction est d'environ 0.00579

              ## L'histogramme des erreurs
err_hist= abs(y-y_predd)
plt.hist(err_hist)
plt.title('Histogramme des erreurs prédits')
plt.xlabel('erreur')
plt.ylabel('pourcentage')
plt.legend()
        #50% des valeurs predit ont une erreur proche de 0
                
              ##Calcul de R^2
r2=r2_score(y,y_predd)
print(r2)
       #Ce modele decrit 64% des variations des  valeurs de stellantis
