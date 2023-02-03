pizzas = ['portuguesa','frango com catupiry','4 queijos']
friend_pizzas = pizzas[:]

pizzas.append("marguerita")
friend_pizzas.append("mista")

for i in pizzas:
    print(f"Minhas pizzas favoritas são: {i.title()}")
for x in friend_pizzas:
    print(f"As pizzas favoritas do meu amigo são: {x.title()}")
