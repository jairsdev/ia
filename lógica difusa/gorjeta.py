"""O objetivo desse problema é encontrar uma gorjeta ideal baseado no nível de atendimento e qualidade da comida.
A lógica difusa é aplicada tanto no antendimento quanto na comida, já que o usuário tem mais de 2 tipos de avaliação disponível.
A biblioteca utilizada para representar a lógica difusa será a SciKit-Fuzzy."""

import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
atendimento = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

print(gorjeta.universe)