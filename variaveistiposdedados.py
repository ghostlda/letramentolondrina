nome = "William"
idade = "quarenta"
altura = 1.75
peso = 80
imc = peso / (altura * altura)

print("Ola Mundo")
print(type(nome))
print(type(idade))
print(type(altura))
print(type(peso))


print("Meu nome é", nome,"tenho", idade, "anos", "possuo ", altura, "de altura", "meu peso é ",peso , "kg")

aluno = input("Digite o nome do aluno: ")
print("Olá ",aluno," bem vindo a escola")

frase = "Pyton é uma linguagem de programação incrível"
print(frase)
frase_maisucula = frase.upper()
print("A frase em maisucula é: ", frase_maisucula)
frase_minuscula = frase.lower()
print("A frase em minuscula é: ", frase_minuscula)
print(frase.replace("incrível" , "legal"))

print ( "-------------")
#tipos de dados: int

idade = 18
print(idade)
print(type(idade))
print(idade+2)
print(float(idade))

print("-------------------")
#tipos de dados: float
altura = 1.75
print(altura)
print(type(altura))
print(altura+2)
print(int(altura))

import math

print(math.ceil(altura))
print(math.floor(altura))
print(math.sqrt(altura))
print(math.pow(altura,2))

complexo = 3 +5j
print(complexo)
print(type(complexo))
print(complexo.real)
print(complexo.imag)

complexo2 = 7 + 10j

soma = complexo+complexo2
print(soma)
n1 = 3.6099
print ("n1 =", round(n1,2))

print ("----------------------")

#tipo de dados booleanos
booleano1 = True
booleano2 = False
print(type(booleano1))
print(booleano1)
print(booleano2)
print(booleano1 and booleano2)
print(booleano1 or booleano2)
print(not booleano1)

print(5>4)

print("-----------`-------")
#tipo de dados : lista
nomes = ["Marcelo", "Josi", "William", "Mirella"]
numeros = [1, 2, 3, 4, 5]
misturado = [8, "Mirella", 5.6, True, "William"]

print("A Lists de nomes é: ", nomes)

print(type(nomes))

print("A lista de numeros é: ", numeros)
print("A posição 0 de nomes contém: ", nomes[0])
print("Aposição 0 de número contém: ",numeros[1])

print(type(numeros))

print(misturado)

print("A lista nomes contém :",len(nomes), "objetos")
print("Alista números contém: ", len(numeros), "objetos")
print(len(misturado))
numeros.append(6)
print(numeros)
numeros.remove(1)
print(numeros)

print("---------------------")

#tipo de dados: tupla
tupla = ("Josi", "William", "Mirella")
print(tupla)
print(type(tupla))
#tupla.append(1)
print(tupla[0])
print(tupla[1])
print(tupla[2])	

print("---------------------")
#tipo de dados: set
numeral = {1, 2, 3, 4, 5, 6}
print((len(numeral)))

conjunto = {3, 5, 8, 9}
intersecao = numeral & conjunto
print(intersecao)

uniao = numeral | conjunto
print(uniao)

diferenca = numeral - conjunto
print(diferenca)

uniao.add(7)
print(uniao)

uniao.remove(9)
print(uniao)

print("------------------")

#tipo de dados: dicionario
pessoa = {
	"nome": "William",
	"idade": 18,
	"altura": 1.75,
	"peso": 81.5,
  "cidade": "Londrina"
}
print(pessoa)
print(type(pessoa))
notas = { "portugues": 6, "matematica": 8, "geografia": 7 }
print(notas)
print(pessoa["nome"])
print(notas["portugues"])

pessoa["endereço"] = "Rua Xyz, 12"
print(pessoa)
print(pessoa.get("endereço"))
pessoa.pop("cidade")
print(pessoa)
pessoa.clear()
print(pessoa)

lista_pessoas = [
  {"nome": "Luca", "idade:" : 18, "cidade": "Campinas"},
  {"nome": "Maria", "idade": 20, "cidade": "Londrina"},
  {"nome": "João", "idade": 35, "cidade": "São Paulo"}
]

print(lista_pessoas)

print("---------------------")
