"""          Regression polynomiale       """
#Regression polynomiale permet de regresser pour des formes de courbes
#Objectif: on cherche le graphe colle le plus au nuage de points

                        ## Les bibliothéques
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


                       ## Importation la data
data= pd.read_csv('stellantis')
t=data.iloc[:,:-2].values  #pas
y=data.iloc[:,-1].values #val
x=data.iloc[:,1].values # temps 
 
                      ## Le nuage de points 
plt.scatter(x, y, color="green",marker = '+',label='')
plt.title('Evolution')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.legend()
plt.show()

                     ##construction du modele de regression polynomiale ##
#Reg_poly consiste a faire varier le degrée du polynome afin d'avoir 
#un meilleur graphe qui ajuste au mieux le nuage de points

poly_reg=PolynomialFeatures(degree= 9)
#On fait varier 'degree' pour avoir un graphe qui colle le mieux 
#au graphe des valeurs
x_poly= poly_reg.fit_transform(t)
regressor2= LinearRegression()
regressor2.fit(x_poly,y)

                      ## Definir la prediction
y_poly_pred=regressor2.predict(x_poly)
                     ##Visualisation des resultats ##
plt.scatter(x, y, color="green",marker = '+',label='')
plt.plot(x,regressor2.predict(x_poly),color="blue",label='graphe')
plt.title('Evolution de Stellantis en environ 17 minutes')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.legend()
plt.show

                      ##Faire quelques predictions futurs
t_futur= poly_reg.fit_transform([[133],[140],[146],[150],[155],[160],[165],
                                 [170],[175],[180],[185],[190],[198]])
regressor2.predict(t_futur)

                     ## Evaluation du modele
# Calcul du MAE
print('MAE:', mean_absolute_error(y,y_poly_pred))

# Calcul du MSE
print('MSE:', sqrt(mean_squared_error(y,y_poly_pred)))
     #L'erreur entre y et y_pred est n'est pas tres grande 
     
# Median absolute error
print('median abs err:', median_absolute_error(y,y_poly_pred))
    #l'erreur de prediction est d'environ 0.00366
    
                   ## L'histogramme des erreurs 
err_hist= abs(y-y_poly_pred)
plt.hist(err_hist)
plt.title('Histogramme des erreurs prédits')
plt.xlabel('erreur')
plt.ylabel('pourcentage')
plt.legend()
    #35% des valeurs predit ont une erreur proche de 0
    
                   ## Calcul de R^2
r2_poly=r2_score(y,y_poly_pred)
print(r2_poly)
    #Ce modele decrit 90% des variations des  valeurs de stellantis
