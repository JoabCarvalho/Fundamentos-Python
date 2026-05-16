oiMundo = "Oi Mundo!"
print(oiMundo)
#----------------------------------
soma = 2+2
print(soma)
#----------------------------------
lista = list(range(1,21))
print(lista)
#----------------------------------
from datetime import date

anoAtual = date.today()
anoNascimento = int(input("Digite o ano de nascimento do seu filho: "))
idade = anoAtual.year - anoNascimento

print(f"Meu filho tem {idade} anos.")
#----------------------------------
import math

raizQuadradaDe = input("Digite um número para obter a raíz quadrada dele: ")
try:
    # Converte a entrada para float antes de calcular a raiz quadrada
    numero_flutuante = float(raizQuadradaDe)
    resultado = math.sqrt(numero_flutuante)
    print(f"A raiz quadrada de {raizQuadradaDe} é: {resultado}")
except ValueError:
    print(f"Erro: '{raizQuadradaDe}' não é um número válido. Por favor, digite um número.")
#----------------------------------