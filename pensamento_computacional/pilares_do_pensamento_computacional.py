# abstração -> representação da realidade e filtragem dos passos essenciais
# decomposição -> quebra do problema maior em problema menores
# reconhecimento de padrões -> reuso de soluções genéricas
# algoritmo -> listagem de passos para a resolução da problemática em questão




print('Olá, seja bem vindo ao algoritmo de potenciação!')
base = int(input('Digite uma base:'))
expoente = int(input('Digite um expoente:'))
i = 1
resultado = 1
for i in range(expoente):
    resultado *= base
print(resultado)