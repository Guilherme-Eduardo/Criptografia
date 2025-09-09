# Trabalho 1 realizado por Guilherme Eduardo & Heloisa Pinho
# GRR20231950 & GRR20231961
# Disciplina: Criptografia

import re
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[i])):
            print (matrix[i][j], end=" ")
        print ("")
    
# Cria a matriz de play fair inicial
def createPlayfairMatrix(key):
    #Concateno o alfabeto na chave
    key = key.replace('J', 'I').upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    # Remove letras repetidas
    key = "".join(dict.fromkeys(key))
    
    matrix = []
    # i vai ser 0, 5, 10, 15, 20. Incrementa os valores na matriz
    for i in range(0, 25, 5):
        line = []
        for k in key[i:i+5]:
            line.append(k)
        matrix.append(line)
    
    return matrix 

# Faz a transposição entre o primeiro, ultimo e o valor do ultimo elemento na tab. ASCII    
def transposition(matrix):
    #Pega o primeiro elemento
    first = matrix[0][0]
    
    #Guarda o ultima caracter da 1° linha e pega o seu valor na tabela ASCII
    lineLastChar = matrix[0][4]
    valueLastChar = ord(lineLastChar)   #Valor na Tab. ASCII
    digits = str(valueLastChar)         #Somo os Digitos
    sum_digits = sum(int(d) for d in digits)

    # Calcula posição válida na matriz
    index = (sum_digits % 25) - 1
    line = int(index / 5)
    column = index % 5

    #Transposição (Triângulo de Guilherme)
    matrix[0][0] = lineLastChar
    matrix[0][4] = matrix[line][column]
    matrix[line][column] = first  
    return index, matrix

# Todo o processo de criptografia da playfair
def playfairDecript(text, key):
#Cria a matriz e já faz a transposição
    matrix = createPlayfairMatrix(key)
    print ("Matriz inicial: ")
    printMatrix(matrix)
    valueLastChar, matrix = transposition(matrix)
    print ("Matriz com transposicao: ")
    printMatrix(matrix)
    


def pizaoDecrypt(encryptFile, decryptFile, key):
    try:
        #Leitura do arquivo
        with open(encryptFile, "r", encoding="utf-8") as f:
            encryptedText = f.read() 
        print(f"texto criptografado: {encryptedText}")      
    except Exception as e:
        print(f"Ocorreu um erro ao criptografar com Pizao: {e}")
        return   
    playfairDecript(encryptedText,key)



# Referência para o alg. AES: https://medium.com/@dheeraj.mickey/how-to-encrypt-and-decrypt-files-in-python-using-aes-a-step-by-step-guide-d0eb6f525e4e

# Remove o preenchimento (padding) adicionado durante a criptografia caso necessario 
def unpad(data):
    padding_length = data[-1]
    if padding_length < 1 or padding_length > 16:
        raise ValueError("Invalid padding encountered")
    return data[:-padding_length]


def aesDecrypt(key, iv, input_file, output_file):
    try:
        # Converte chave e vetor de inicialização de hexadecimal para bytes
        decoded_key = bytes.fromhex(key)
        iv_bytes = bytes.fromhex(iv)

        if len(decoded_key) != 32:
            raise ValueError("Incorrect AES key length")
        cipher = AES.new(decoded_key, AES.MODE_CBC, iv_bytes)

        # Lê os dados criptografados do arquivo de entrada
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()

        # Decripta e remove o padding para obter o texto original
        decrypted_data = unpad(cipher.decrypt(encrypted_data))

        # Salva os dados descriptografados no arquivo de saída
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
