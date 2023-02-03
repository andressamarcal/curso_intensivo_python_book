# Solução do Problema referente ao Capitulo 3, questao 3.5

peoples = ['andressa','aninha','wesley']
print("Wesley não poderá comparecer ao jantar.")
print("Informamos que haverá mais espaços disponíveis nas mesas para o jantar. Abaixo seguirá a lista de convidados.")

peoples[2] = "felipe"

peoples.insert (0, 'alex')
peoples.insert (2, 'gil')
peoples.append('swelton') 

convites = peoples

message = f"Hi {convites} welcome to my dinner!"
#message2 = "Hi " + peoples[1] + " welcome to my dinner!"
#message3 =  "Hi " + peoples[2] + " welcome to my dinner!"

print(message) #message2, message3
