#%pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from typing import get_origin
#Variaveis de Entrada (Antecedent)
comer = ctrl.Antecedent(np.arange(0, 16, 1), 'comer')
tempoAtividade = ctrl.Antecedent(np.arange(0, 11, 1), 'tempo de atividade fisica')

#Variaveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 16, 1), 'peso')

#trapezoidal
comer['pouco'] = fuzz.trapmf(comer.universe, [-1,0,2,4])
comer['razoavel'] = fuzz.trapmf(comer.universe, [2,4,6,8])
comer['bastante'] = fuzz.trapmf(comer.universe, [4,6,15,15])

tempoAtividade['pouco'] = fuzz.trapmf(tempoAtividade.universe, [-1,0,1,4])
tempoAtividade['razoavel'] = fuzz.trapmf(tempoAtividade.universe, [3,4,5,7])
tempoAtividade['bastante'] = fuzz.trapmf(tempoAtividade.universe, [6,8,10,12])

peso['leve'] = fuzz.trapmf(peso.universe, [-1,0,4,6])
peso['medio'] = fuzz.trapmf(peso.universe, [4,6,8,10])
peso['pesado'] = fuzz.trapmf(peso.universe, [8,10,15,15])

#Criando as regras
regra_1 = ctrl.Rule(comer['pouco'] , peso['leve'])
regra_2 = ctrl.Rule(comer['razoavel'] & (tempoAtividade['razoavel'] | tempoAtividade['bastante']), peso['leve'])
regra_3 = ctrl.Rule(comer['razoavel'] , peso['medio'])
regra_5 = ctrl.Rule(comer['bastante'] & tempoAtividade['bastante'], peso['medio'])
regra_4 = ctrl.Rule(comer['bastante'], peso['pesado'])

controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3, regra_4, regra_5])
CalculoPeso = ctrl.ControlSystemSimulation(controlador)

CalculoPeso.input['comer'] = 6
CalculoPeso.input['tempo de atividade fisica'] = 8
#Crunch the numbers
CalculoPeso.compute()

print(CalculoPeso.output['peso'])
comer.view(sim=CalculoPeso)
tempoAtividade.view(sim=CalculoPeso)
peso.view(sim=CalculoPeso)
