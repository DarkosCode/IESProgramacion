import numpy as np
from scipy import special as spc
#* probabilidad = exito / totalidad (*100 para porcentaje%)
#* probabilidad: clasica (a priori) - frecuencial (posteriori) - subjetiva

dado = np.array([1,2,3,4,5,6])

#? CLASICA O A PRIORI
probabX = dado[dado == 3].size / dado.size
#! f para format string
print(f"P(dado = 3) = {probabX * 100:.2f}%") #probabilidad de que el dado sea x numero

probabImp = dado[dado % 2 != 0].size / dado.size
print(f"P(dado impar) = {probabImp * 100:.2f}%") #probabilidad de que el dado sea impar
probabPar = dado[dado % 2 == 0].size / dado.size #probabilidad de que el dado sea par
probabMen = dado[dado < 4].size / dado.size
print(f"P(dado < 4) = {probabMen * 100:.2f}%") #probabilidad de que el dado sea menor a x numero

probabX_o_Par = probabX + probabPar

#? FRECUENCIAL