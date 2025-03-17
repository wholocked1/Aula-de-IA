#Triangular
comer['pouco'] = fuzz.trimf(comer.universe, [-1,0,2])
comer['razoavel'] = fuzz.trimf(comer.universe, [1,4,6])
comer['bastante'] = fuzz.trimf(comer.universe, [4,15,15])

tempoAtividade['pouco'] = fuzz.trimf(tempoAtividade.universe, [-1,0,4])
tempoAtividade['razoavel'] = fuzz.trimf(tempoAtividade.universe, [3,5,6])
tempoAtividade['bastante'] = fuzz.trimf(tempoAtividade.universe, [5,8,10])

peso['leve'] = fuzz.trimf(peso.universe, [-1,0,4])
peso['medio'] = fuzz.trimf(peso.universe, [4,6,8])
peso['pesado'] = fuzz.trimf(peso.universe, [8,15,15])

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
