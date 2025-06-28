import getpass

while True:
    word = getpass.getpass("Digite a palavra secreta: ")
    
    if word == "chupacabra":
        print("Você saiu do loop com sucesso")
        break
    else:
        print("Você ainda está preso no loop")
        
  
   