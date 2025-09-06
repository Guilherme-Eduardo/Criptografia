# Trabalho realizado por Guilherme Eduardo & Heloisa Pinho
# GRR20231950 & GRR20231961
# Disciplina: Criptografia

from cifra import aesEncrypt, pizaoEncrypt


def main():
    # Definindo o nome dos arquivos de que serao usados na criptografia
    inputFile = ['../input.txt', '../documents/Moby Dick; Or, The Whale by Herman Melville - 1,4MB.txt']
    outputPizao = ["../outputPizao"]
    outputAES = ["../outputAES"]
    
    #Definindo o valor da chave
    key = "HELOISA"

    #Usando a nossa ideia de criptografia
    pizaoEncrypt (inputFile[1], outputPizao[0], key)

    # Criptografia com o AES
    print ("\nCriptografando com o AES...")
    key, iv = aesEncrypt(inputFile[1], outputAES[0])
    if key and iv:
        print("Criptografia com o AES finalizada.")
        print("Chave:", key)
        print("Vetor de inicialização:", iv)
        
    print ("Arquivos salvos com sucesso!")

if __name__ == '__main__': 
    main()