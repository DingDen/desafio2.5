def verificacao_estrela_perceptivel(quant_estrelas, area_telescopio):
    estrelas_perceptiveis = 0
    for estrela in quant_estrelas:
        telescopio_verificacao = area_telescopio * estrela
        if(telescopio_verificacao >= 40*10**6):
            estrelas_perceptiveis += 1
    print('Quantidade de estrelas que serão percebidas:', estrelas_perceptiveis)

A = 0

while(not(1 <= A <= 10**4)):
    A = int(input('Área de abertura do telescópio(mm²): '))

N = 0
while(not(1 <= N <= 10**4)):
    N = int(input('Número de estrelas a serem estudadas: '))

quantidade_estrelas = []

for cont in range(N):
    F = 0
    while(not(1 <= F <= 20*10**3)):
        print(cont+1,'estrela -> ', end='')
        F = int(input('Fluxo de fótons: '))
    quantidade_estrelas.append(F)

verificacao_estrela_perceptivel(quantidade_estrelas, A)