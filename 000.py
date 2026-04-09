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

raizDe = input("Digite um número para obter a raíz quadrada dele: ")
try:
    # Converte a entrada para float antes de calcular a raiz quadrada
    numero_flutuante = float(raizDe)
    resultado = math.sqrt(numero_flutuante)
    print(f"A raiz quadrada de {raizDe} é: {resultado}")
except ValueError:
    print(f"Erro: '{raizDe}' não é um número válido. Por favor, digite um número.")
#----------------------------------