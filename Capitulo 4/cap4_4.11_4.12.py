pizzas = ['portuguesa','frango com catupiry','4 queijos']
friend_pizzas = pizzas[:]

pizzas.append("marguerita")
friend_pizzas.append("mista")

for i in pizzas:
    print("Minhas pizzas favoritas são: " +i.title())
for x in friend_pizzas:
    print("As pizzas favoritas do meu amigo são: " +x.title())
