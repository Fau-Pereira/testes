beatles = []# etapa 1

print("Etapa 1:", beatles)


beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")# etapa 2

print("Etapa 2:", beatles)


for _ in range (2):
    member = input("\nDigite o nome do membro Stu Stucliffe:" )
    beatles.append(member)
    member_2 = input("\nDigite o  nome do membro Pete Best:" )# etapa 3
    beatles.append(member_2)
    
print("Etapa 3:", beatles)


del bealtes[3]
del beatles[4]# etapa 4

print("Etapa 4:", beatles)

beatle.insert(3,"Ringo Starr") # passo 5

print("Etapa 5:", beatles)



# testando o tamanho da lista

("o fabuloso", len(beatles))