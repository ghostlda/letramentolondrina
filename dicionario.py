#n1 = int(input("Digite um número:"))
for n1 in range(0,11,2):
  print(f"Numeros pares: {n1}")

for n1 in range(1,11,2):
  print(f"Numeros impares: {n1}")

lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for n1 in lista:
  if type(n1) == int:
    soma = soma+n1
  
print(f"Soma dos numeros na lista é: {soma}")  
somapar = 0
somaimpar = 0 
for numero in lista:
  if numero % 2 == 0:
    somapar += numero
  elif numero % 2 != 0:
    somaimpar += numero
    
print(f"Soma dos numeros pares na lista é: {somapar}, e a soma dos impares é {somaimpar}")
    
print("Soma dos numeros impares: ", somaimpar)

somaimpar = 0
for numero in lista:
  if numero % 2 == 1:
    somaimpar += numero
print("Soma dos numeros impares: ", somaimpar)


notas = {
  "Português":"91", 
  "Matemática":"100",
  "História":"80",
  "Geografia":"90",
  "Ingles": "90",
  "Biologia":"100"
}
materia = input("Digite o nome da matéria")

if materia in notas:
  print(f"A nota da matéria {materia} é {notas[materia]}")
else:
  print("Matéria não encontrada")


