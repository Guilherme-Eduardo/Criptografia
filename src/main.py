# Trabalho realizado por Guilherme Eduardo & Heloisa Pinho
# GRR20231950 & GRR20231961
# Disciplina: Criptografia

from cipher import aesEncrypt, pizaoEncrypt
from decipher import aesDecrypt, pizaoDecrypt
import timeit
from utils import timeEvaluation


def main():
    # Definindo o nome dos arquivos de que serao usados na criptografia
    inputFile = ['../documents/Moby Dick; Or, The Whale by Herman Melville - 1,4MB.txt']
    outputPizao = ["../decryptedPizao.txt"]
    outputAES = ["../decryptedAES.txt"]
    decryptedPizao = ["../decryptedPizao.txt"]
    decryptedAES = ["../decryptedAES.txt"]
    
    #Definindo o valor da chave
    key = "HELOISA"
    
    
    #Usando a nossa ideia de criptografia
    print ("\nCriptografando com o Pizao...")
    pizaoEncInitialTime = timeit.default_timer();
    pizaoEncrypt (inputFile[0], outputPizao[0], key)
    pizaoEncEndTime = timeit.default_timer();
    timeEvaluation ("Pizao", "Cifra", pizaoEncInitialTime, pizaoEncEndTime)
    

    #Descriptografando nossa cifra 
    pizaoDecInitialTime = timeit.default_timer();
    pizaoDecrypt(outputPizao[0],decryptedPizao[0], key)
    pizaoDecEndTime = timeit.default_timer();
    print("Arquivo decifrado com sucesso usando Pizao.")
    timeEvaluation ("Pizao", "Decifra", pizaoDecInitialTime, pizaoDecEndTime)

    #Criptografia com o AES
    aesEncInitialTime = timeit.default_timer();
    key, iv = aesEncrypt(inputFile[0], outputAES[0])
    aesEncEndTime = timeit.default_timer();
    if key and iv:
        timeEvaluation ("AES", "Cifra", aesEncInitialTime, aesEncEndTime)
        print("Criptografia com o AES finalizada.")
        print("Chave:", key)
        print("Vetor de inicialização:", iv)
        aesDecInitialTime = timeit.default_timer();
        aesDecrypt(key, iv, outputAES[0], decryptedAES[0])
        aesDecEndTime = timeit.default_timer();
        timeEvaluation ("AES", "Decifra", aesDecInitialTime, aesDecEndTime)

        print("Arquivo decifrado com sucesso usando AES.")
    else:
        print("Falha na criptografia usando AES")
        
    print ("Arquivos salvos com sucesso!")

if __name__ == '__main__': 
    main()