# Trabalho realizado por Guilherme Eduardo & Heloisa Pinho
# GRR20231950 & GRR20231961
# Disciplina: Criptografia

from cifra import aesEncrypt, pizaoEncrypt
from decifra import aesDecrypt, pizaoDecrypt


def main():
    # Definindo o nome dos arquivos de que serao usados na criptografia
    inputFile = ['../input.txt', '../documents/Moby Dick; Or, The Whale by Herman Melville - 1,4MB.txt']
    outputPizao = ["../outputPizao"]
    outputAES = ["../outputAES"]
    decryptedPizao = ["../decryptedPizao"]
    decryptedAES = ["../decryptedAES"]
    
    #Definindo o valor da chave
    key = "HELOISA"

    print ("\nCriptografando com o Pizao...")
    #Usando a nossa ideia de criptografia
    pizaoEncrypt (inputFile[1], outputPizao[0], key)

    #Descriptografando nossa cifra 
    pizaoDecrypt(outputPizao[0],decryptedPizao[0], key)

    print("Arquivo decifrado com sucesso usando Pizao.")

    #Criptografia com o AES
    print ("\nCriptografando com o AES...")
    key, iv = aesEncrypt(inputFile[1], outputAES[0])
    if key and iv:
        print("Criptografia com o AES finalizada.")
        print("Chave:", key)
        print("Vetor de inicialização:", iv)
        aesDecrypt(key, iv, outputAES[0], decryptedAES[0])
        print("Arquivo decifrado com sucesso usando AES.")
    else:
        print("Falha na criptografia usando AES")
        
    print ("Arquivos salvos com sucesso!")

if __name__ == '__main__': 
    main()