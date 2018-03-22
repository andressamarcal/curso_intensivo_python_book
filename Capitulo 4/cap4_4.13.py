# tupla de itens
foods = ('arroz','feijao','macarrao','frango','carne')

# percorre e exibe os itens do cardapio
for f in foods:
    print(f)

# erro de alteração de valores, devido estar lidando com estrutura Tupla (imultavel)
#foods[0] = 'salada'

#mudando valores da variavel tupla, ou seja, sobrescrevendo-os.
foods = ('file','arroz a grega','feijao preto','carne acebolada','batata frita')

#exibindo tupla sobrescrita
for i in foods:
    print(i)