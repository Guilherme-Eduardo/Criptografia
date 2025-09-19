# Trabalho realizado por Guilherme Eduardo & Heloisa Pinho
# GRR20231950 & GRR20231961
# Disciplina: Criptografia

from cipher import aesEncrypt, pizaoEncrypt
from decipher import aesDecrypt, pizaoDecrypt
import timeit
from utils import timeEvaluation


def main():
    # Definindo o nome dos arquivos de que serao usados na criptografia
    inputFile = [
        '../documents/Moby Dick; Or, The Whale by Herman Melville - 1,4MB.txt',
        '../documents/Moby Multiple Language Lists of Common Words by Grady Ward - 22 kB.txt',
        '../documents/Romeo and Juliet by William Shakespeare - 100KB.txt'
    ]
    
    # Definindo os nomes dos arquivos de saída (Cifra/Decifra)
    pizaoDecryptedFilePath = [
        "../results/decryptedPizao-Moby Dick.txt",
        "../results/decryptedPizao-Moby Multiple.txt",
        "../results/decryptedPizao-Romeo and Juliet.txt"        
    ]
    
    pizaoEncFilePath = [
        "../results/EncryptedPizao-Moby Dick.txt",
        "../results/EncryptedPizao-Moby Multiple.txt",
        "../results/EncryptedPizao-Romeo and Juliet.txt"        
    ]
    
    aesDecryptedFilePath = [
        "../results/decryptedAES-Moby Dick.txt",
        "../results/decryptedAES-Moby Multiple.txt",
        "../results/decryptedAES-Romeo and Juliet.txt" 
    ]
    
    aesEncFilePath = [
        "../results/EncryptedAES-Moby Dick.bin",
        "../results/EncryptedAES-Moby Multiple.bin",
        "../results/EncryptedAES-Romeo and Juliet.bin" 
    ]
    
    
    #Definindo o valor da chave
    pizaoKey = "HELOISA"
    
    for i in range(len(inputFile)):
        #Usando a nossa ideia de criptografia
        pizaoEncInitialTime = timeit.default_timer();
        pizaoEncrypt (inputFile[i], pizaoEncFilePath[i], pizaoKey)
        pizaoEncEndTime = timeit.default_timer();
        timeEvaluation ("Pizao", "Cifra", pizaoEncInitialTime, pizaoEncEndTime)
        

        #Descriptografando nossa cifra         
        pizaoDecInitialTime = timeit.default_timer();
        pizaoDecrypt(pizaoEncFilePath[i], pizaoDecryptedFilePath[i], pizaoKey)
        pizaoDecEndTime = timeit.default_timer();        
        timeEvaluation ("Pizao", "Decifra", pizaoDecInitialTime, pizaoDecEndTime)
        

        #Criptografia com o AES
        aesEncInitialTime = timeit.default_timer();
        aesKey, iv = aesEncrypt(inputFile[i], aesEncFilePath[i])
        aesEncEndTime = timeit.default_timer();
        if aesKey and iv:
            timeEvaluation ("AES", "Cifra", aesEncInitialTime, aesEncEndTime)
            print("Criptografia com o AES finalizada.")
            print("Chave:", aesKey)
            print("Vetor de inicialização:", iv)
            aesDecInitialTime = timeit.default_timer();
            aesDecrypt(aesKey, iv, aesEncFilePath[i], aesDecryptedFilePath[i])
            aesDecEndTime = timeit.default_timer();
            timeEvaluation ("AES", "Decifra", aesDecInitialTime, aesDecEndTime)

            print("Arquivo decifrado com sucesso usando AES.")
        else:
            print("Falha na criptografia usando AES")
            
        print ("Arquivos salvos com sucesso!")

if __name__ == '__main__': 
    main()