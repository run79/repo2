#1º Faça um programa que pergunta a idade do usuário e informe se ele está apto a votar ou não.

# idade = int(input("Digite sua idade? "))
# if idade >= 18 and idade < 70:
#         print("Voto obrigatório!")
# elif idade <= 18 and idade >= 16:
#     print("Voto opicional!")
# else: 
#     print(idade <16, "Voto inválido!")

#2º Faça um Programa que leia três números inteiros e mostre o maior deles.
# n1 = int(input("Primeiro nº: " ))
# n2 = int(input("Segundo nº: " ))
# n3 = int(input("Teceiro nº: " ))
# if n1 > n2 and n1 > n3:
#     print("O primeiro nº é maior: ")
# elif n2 > n1 and n2 > n3:
#     print("O segundo nº é maior: ")
# elif n3 > n1 and n3 > n2:
#     print("O terceiro nº é maior: " )
# else:
#     print(f"n/d")
#     print(f"FIM")

#3º Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
# n1 = int(input("Primeiro nº: " ))
# n2 = int(input("Segundo nº: " ))
# n3 = int(input("Teceiro nº: " ))
# menor = n1
# if n2<n1 and n2<n3:
#    menor = n2
# if n3<n1 and n3<n2:

#     menor = n3
# print('o menor valor é: {} '.format(menor))
# maior = n1
# if n2>n1 and n2>n3:
#     maior = n2
# if n3>n1 and n3>n2:
#     maior = n3
# print('o maior valor é: {}'.format(maior))

#4º Faça um programa, utilizando while, que mostre na tela os números de 0 a 100.
# contador = 0
# while (contador < 101):
#        print(contador)
#        contador   = contador + 1
# numero = 0
# while numero<=100:
#     print(numero)
#     numero+=1 # O mesmo que numero = numero + 1


# 5º Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite inserido pelo usuário.
# inicio = 0
# limite = int(input("Digite um numero:"))
# while inicio<= limite:
#     print(inicio)
#     inicio = inicio + 1

#6º Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas e os 
# mostre na tela.
# Dark = ["Martha", "Jonas", "Agnes", "Claudia", "Michael", "Ulrich", "Eva", "Adam"]
# indice = 0
# indice_final = len(Dark) - 1
# while indice <= indice_final:
#     print(Dark[indice])
#     indice+=1

#7º Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

# n1=int(input("Digite o primeiro número: "))
# n2=int(input("Digite o segundo número: "))
# soma = n1 + n2
# print(soma)
# resposta=str(input("Deseja realizar uma nova soma (S)-SIM , (N)-Não: ")).upper()
# while resposta == "S":
#     n1=int(input("Digite o primeiro número: "))
#     n2=int(input("Digite o segundo número: "))
#     soma = n1 + n2
#     print(soma)
#     resposta=str(input("Deseja realizar uma nova soma (S)-SIM , (N)-Não: ")).upper()
# else:
#     print("Total finalizado!!! ")

# 8º Faça um programa, utilizando while e listas, que permita o usuário realizar o cadastro de um
#  número indeterminado de pessoas enquanto quiser e os mostre na tela ao finalizar.
# lista = []
# while True:
#     nome = input("Digite o nome: ")
#     lista.append(nome)
#     if nome == "sair":
#         lista.remove("sair")
#         print(lista)
#         break

#9º Faça um programa que imprima a quantidade de números pares entre dois números da sua escolha.
# def contaPares(lista):
#     pares = 0
#     impares = 0
#     for num in lista:
#         if (num % 2) == 0:
#             pares = pares + 1
#         else:
#             impares = impares + 1
#     return pares, impares
# lista = list() 
# q = int(input('Quantos valores haverá na lista ?'))
# while q < 0:
#     print('Erro')
#     q = int(input('Quantos valores haverá na lista ?'))
# for c in range(q):
#     num = int(input('Valor:'))
#     lista.append(num)
# print('A quantidade de valores pares e impares são, respectivamente:',contaPares(lista))


# 10ºFaça um programa que imprima a soma de todos os números pares entre dois números da sua escolha.
# def somalista(numeros):
#    if len(numeros) == 1:
#         return numeros[0]
#    else:
#         return numeros[0] + somalista(numeros[1:])
# print(somalista([2,4]))




