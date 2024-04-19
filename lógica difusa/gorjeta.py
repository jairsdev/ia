"""O objetivo desse problema é encontrar uma gorjeta ideal baseado no nível de atendimento e qualidade da comida.
A lógica difusa é aplicada tanto no antendimento quanto na comida, já que o usuário tem mais de 2 tipos de avaliação disponível.
A biblioteca utilizada para representar a lógica difusa será a SciKit-Fuzzy."""

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
atendimento = ctrl.Antecedent(np.arange(0, 11, 1), 'atendimento')
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
atendimento.automf(number=3, names=['ruim', 'aceitavel', 'otimo'])

"""gorjeta['baixa'] = fuzzy.trimf(gorjeta.universe, [0, 0, 8])
gorjeta['media'] = fuzzy.trimf(gorjeta.universe, [2, 10, 18])
gorjeta['alta'] = fuzzy.trimf(gorjeta.universe, [12, 20, 20])"""

gorjeta['baixa'] = fuzzy.pimf(gorjeta.universe, )
gorjeta['media'] = fuzzy.pimf(gorjeta.universe, 5, -1)
gorjeta['alta'] = fuzzy.pimf(gorjeta.universe, 10, -1)  

regra1 = ctrl.Rule(qualidade['ruim'] | atendimento['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(atendimento['aceitavel'], gorjeta['media'])
regra3 = ctrl.Rule(qualidade['saborosa'] | atendimento['otimo'], gorjeta['alta'])

sistemaControle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistemaControle)
sistema.input['qualidade'] = 10
sistema.input['atendimento'] = 10
sistema.compute()
print(sistema.output['gorjeta'])
gorjeta.view(sim=sistema)
plt.show()

