my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Escreva seu código aqui.
# A abordagem recomendada é criar uma nova lista para armazenar os elementos únicos.
new_list = []

for number in my_list:
    # Se o número ainda não estiver na nossa nova lista, nós o adicionamos.
    if number not in new_list:
        new_list.append(number)

# A lista original agora pode ser substituída pela lista de itens exclusivos.
my_list = new_list

print("A lista com os elementos exclusivos aqui:")
print(my_list)
