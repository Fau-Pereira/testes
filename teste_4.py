blocks = int(input("Insira o número de blocos:"))  

altura = 0
blocos_proxima_camada = 1

while blocks >= blocos_proxima_camada:
    blocks -= blocos_proxima_camada
    altura += 1
    blocos_proxima_camada += 1
    
print("A altura da pirâmide:", altura)