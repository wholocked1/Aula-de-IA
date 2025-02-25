#pip install 
#pip install matplotlib
#pip install pandas

import pandas as pd
import numpy as np
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from scipy.io import arff


data,meta = arff.loadarff('./TempoPartidaTenis.arff')

attributes = meta.names()
data_value = np.asarray(data)


tempo = np.asarray(data['Tempo']).reshape(-1,1)
temperatura = np.asarray(data['Temperatur']).reshape(-1,1)
umidade = np.asarray(data['Umidade']).reshape(-1,1)
vento = np.asarray(data['Vento']).reshape(-1,1)
features = np.concatenate((tempo, temperatura,umidade,vento),axis=1)
target = data['Partida']


Arvore = DecisionTreeClassifier(criterion='entropy').fit(features, target)

plt.figure(figsize=(10, 6.5))
tree.plot_tree(Arvore,feature_names=['Tempo','Temperatura','Umidade','Vento'],class_names=['Nao', 'Sim'],
                   filled=True, rounded=True)
plt.show()

fig, ax = plt.subplots(figsize=(25, 10))
metrics.ConfusionMatrixDisplay.from_estimator(Arvore,features,target,display_labels=['Nao', 'Sim'], values_format='d', ax=ax)
plt.show()
