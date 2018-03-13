# Solução do Problema referente ao Capitulo 3, questao 3.6

peoples = ['andressa','aninha','wesley']
peoples[2] = "felipe"
peoples.insert (0, 'alex') 
peoples.insert (2, 'gil')
peoples.append('swelton') 

print("Informamos que devido problemas tecnicos, só poderemos convidar duas pessoas.")

desconvidados = peoples.pop(0), peoples.pop(1), peoples.pop(2), peoples.pop()
#comando pop sem paramento, remove por padrão o ultimo da list
print("Desculpe-nos " + str(desconvidados) + " sentimos muito por não poder convida-los mais.")

convidados = peoples

message = "Hi " + str(convidados) + " welcome to my dinner!"
print(message)

del convidados[1]
del convidados[0]

print (peoples)