# TESTE ESTÁGIO 


"""Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
"""

# Resolução

indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k
    print(soma)

# Resposta: o valor da variável SOMA será 91.

"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

# Resolução

nums = [0, 1]

input_num = 3

if input_num < 0:
    print(f'o numero {input_num} não pertence a sequencia')

else:
    while nums[-1] < input_num:
        nums.append(nums[-1] + nums[-2])

    if input_num in nums:
        print(f'o numero {input_num} pertence a sequencia.')
    else:
        print(f'o numero {input_num} não pertence a sequencia.')


"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""

# Resolução

import json

with open('dados.json', 'r') as file:
    faturamento = json.load(file)

menor_valor = min(item['valor'] for item in faturamento if item['valor'] > 0)
print(menor_valor)

maior_valor = max(item['valor'] for item in faturamento)
print(maior_valor)

total = sum(item['valor'] for item in faturamento)
dias = len(faturamento)

media_mensal = total / dias if dias > 0 else 0

print(f'A média mensal é: {media_mensal}')

sup_media_mensal = sum(1 for item in faturamento if item['valor'] > media_mensal)
print(f'Número de dias em que o faturamento diário foi maior que a média mensal: {sup_media_mensal}')



"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
"""

# Resolução
estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}


total = sum(estados.values())

def calcular_percentual(estado):
    percentual = (estado / total) * 100
    print(f'Percentual: {percentual:.2f}%')

for estado, valor in estados.items():
    print(f"{estado}: ", end="")
    calcular_percentual(valor)


"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

# Resolução

input_string = 'exemplo' 

reverse_list = []


for letra in input_string:
    reverse_list.append(letra)

    reverse_string_no_comma = ''.join(reverse_list)
    result = reverse_string_no_comma.replace('\n', '')

print(result)

    