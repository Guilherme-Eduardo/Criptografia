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

# Encontra as posições de linha e coluna da respectiva letra na matriz playfair
def findPositionMatrix(matrix, char):
    line = 0
    column = 0
    
    # Se o char for 'J, substitui por I
    char = 'I' if char == 'J' else char
    
    #Encontra linha e coluna na matriz
    for i in range (0, len(matrix)):        
        for j in range (0, len(matrix[i])):
            if (char == matrix[i][j]):
                line = i
                column = j
                return line, column

# Responsável por fazer as substituições na cifra Playfair (decifração)
def playfairSubstitutionDec(matrix, line1, line2, column1, column2):
    # mesma linha
    if line1 == line2:
        # anda uma coluna para a esquerda (volta ao final se estiver na primeira coluna)
        char1 = 4 if column1 == 0 else column1 - 1
        char2 = 4 if column2 == 0 else column2 - 1
        return matrix[line1][char1], matrix[line2][char2]

    # mesma coluna
    elif column1 == column2:
        # anda uma linha para cima (volta ao final se estiver na primeira linha)
        char1 = 4 if line1 == 0 else line1 - 1
        char2 = 4 if line2 == 0 else line2 - 1
        return matrix[char1][column1], matrix[char2][column2]

    # retângulo (troca as colunas)
    else:
        return matrix[line1][column2], matrix[line2][column1]

def cesarDecrypt(text, value):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    decryptedText = ""
    
    for ch in text:
        if ch.isdigit():  
            # mantém números sem alteração
            decryptedText += ch
        else:
            # aplica o deslocamento da César apenas em letras
            position = (alphabet.index(ch) - (value + 1)) % len(alphabet)
            decryptedText += alphabet[position]
            
    #print ("Texto decifrado com a cifra de Cesar: ", decryptedText)

    return decryptedText
    
# Função para decifrar todo o processo Playfair + César
def textDecrypt(text, key):
    # Cria matriz Playfair e aplica transposição
    matrix = createPlayfairMatrix(key)
    print("Matriz inicial:")
    printMatrix(matrix)
    
    # Consegue o valor para decifrar a cifra de Cesar
    valueLastChar, matrix = transposition(matrix)
    print("Matriz com transposicao:")
    printMatrix(matrix)

    # Primeiro decifra César
    decryptedText = cesarDecrypt(text, valueLastChar)

    finalText = ""
    i = 0
    while i < len(decryptedText):
        ch = decryptedText[i]

        # Se for número, copia direto
        if ch.isdigit():
            finalText += ch
            i += 1
            continue

        # Garante sempre um par de letras
        if i + 1 >= len(decryptedText) or decryptedText[i+1].isdigit():
            pair = ch + "X"
            i += 1
        else:
            pair = decryptedText[i:i+2]
            i += 2

        # Localiza posições na matriz
        line1, col1 = findPositionMatrix(matrix, pair[0])
        line2, col2 = findPositionMatrix(matrix, pair[1])

        # Aplica substituição inversa Playfair
        l1, l2 = playfairSubstitutionDec(matrix, line1, line2, col1, col2)
        finalText += l1 + l2

    # Remove X de padding, considerando números no final
    if finalText.endswith("X") and not finalText[-1].isdigit():
        finalText = finalText[:-1]
    elif len(finalText) > 1 and finalText[-2] == "X" and finalText[-1].isdigit():
        finalText = finalText[:-2] + finalText[-1]

    #print("Texto decifrado com a cifra de PlayFair:", finalText)
    return finalText


# Função para ler arquivo criptografado e aplicar decifragem Pizão
def pizaoDecrypt(encryptFile, decryptFile, key):
    try:
        with open(encryptFile, "r", encoding="utf-8") as f:
            encryptedText = f.read()
        #print(f"Texto criptografado: {encryptedText}")
    except Exception as e:
        print(f"Erro ao ler arquivo criptografado: {e}")
        return

    # Decifra o texto
    print ("Decifrando com o nosso algoritmo (Pizao)!")        
    finalText = textDecrypt(encryptedText, key)

    # Salva o resultado no arquivo de saída
    try:
        with open(decryptFile, "w", encoding="utf-8") as f:
            f.write(finalText)
        print("Arquivo decifrado salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar arquivo decifrado: {e}")


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
