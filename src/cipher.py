# Trabalho 1 realizado por Guilherme Eduardo & Heloisa Pinho
# GRR20231950 & GRR20231961
# Disciplina: Criptografia


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from utils import printMatrix, formatFile



# Imprime as informações inicias
def initialInfo(key, text, matrix, valueLastChar):
    print (f"\nChave: {key}")
    print ("Soma do ultimo digito da 1° da linha da tab. ASCII: ", valueLastChar)
    #print (f"Texto Claro: {text}")
    print ("\nMatriz após a transposicao")
    printMatrix(matrix)
    
    

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
            
    return findPositionMatrix(matrix, 'X')

# Responsavel por fazer as substituções na cifra e retorna as letras para serem concatenadas
def playfairSubstitutionEnc(matrix, line1, line2, column1, column2):
    # mesma linha
    if line1 == line2:
        char1 = 0 if column1 == 4 else column1 + 1
        char2 = 0 if column2 == 4 else column2 + 1
        return matrix[line1][char1], matrix[line2][char2]

    # mesma coluna
    elif column1 == column2:
        char1 = 0 if line1 == 4 else line1 + 1
        char2 = 0 if line2 == 4 else line2 + 1
        return matrix[char1][column1], matrix[char2][column2]

    else:
        return matrix[line1][column2], matrix[line2][column1]



# Todo o processo de criptografia da playfair
def playfairEncript(text, key):
    
    #Cria a matriz e já faz a transposição
    matrix = createPlayfairMatrix(key)
    print ("Matriz inicial: ")
    printMatrix(matrix)
    valueLastChar, matrix = transposition(matrix)
    
    initialInfo(key, text, matrix, valueLastChar)
    
    #Variavel que ficará o texto cifrado
    encryptedText = ""

    i = 0
    while i < len(text):
        # Se o caractere for número o mantem no resultado
        if text[i].isdigit():
            encryptedText += text[i]
            i += 1
            continue

        # Garante que sempre tera um par de letras
        if i + 1 >= len(text) or text[i+1].isdigit():
            pairLetters = text[i] + "X"
            i += 1
        else:
            pairLetters = text[i:i+2]
            i += 2

        # Localiza posições
        line1, column1 = findPositionMatrix(matrix, pairLetters[0])
        line2, column2 = findPositionMatrix(matrix, pairLetters[1])

        # Faz substituição e concatena
        l1, l2 = playfairSubstitutionEnc(matrix, line1, line2, column1, column2)
        encryptedText += l1 + l2
        
    #print ("Texto cifrado com a cifra de PlayFair: ", encryptedText)    
    return valueLastChar, encryptedText

    
    
def cesarEncrypt(text, value):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    encryptedText = ""
    
    for ch in text:
        if ch.isdigit():  
            # mantém os números sem alterar
            encryptedText += ch
        else:
                position = (alphabet.index(ch) + value + 1) % len(alphabet)
                encryptedText += alphabet[position]
            
    #print ("Texto cifrado com a cifra de Cesar: ", encryptedText)
    return encryptedText
    
    
def pizaoEncrypt(inputFile, outputFile, key):
    try:
        #Leitura do arquivo
        with open(inputFile, "r", encoding="utf-8") as f:
            cleanText = f.read()       
    except Exception as e:
        print(f"Ocorreu um erro ao criptografar com Pizao: {e}")
        return    
    
    print ("\n\nIniciando a criptografia com o nosso algoritmo (Pizao)!")
    cleanText = formatFile(cleanText)
    value, encryptedTextPF = playfairEncript(cleanText, key)
    encryptedTextC = cesarEncrypt (encryptedTextPF, value)    
    #print ("resultado final do Alg Pizao: ", encryptedTextC)
    
    with open(outputFile, 'w') as f:
        f.write(encryptedTextC)
    
    
# Referência para o alg. AES: https://medium.com/@dheeraj.mickey/how-to-encrypt-and-decrypt-files-in-python-using-aes-a-step-by-step-guide-d0eb6f525e4e

# Dados devem ser multiplos de 16 bytes. Caso contrario, precisaremos preencher
def pad(data):
    padding_length = 16 - len(data) % 16
    padding = bytes([padding_length] * padding_length)
    return data + padding


def aesEncrypt(input_file, output_file):
    # Gera valores aleatorios em bytes (Questões de segurança)
    key = get_random_bytes(32)      # Chave
    iv = get_random_bytes(16)       # Vetor de inicialização
    cipher = AES.new (key, AES.MODE_CBC, iv)
    try:
        #Leitura do arquivo
        with open (input_file, 'rb') as f:
            plaintext = f.read()
        # Realiza o preenchiemtno
        padded_plaintext = pad(plaintext)
        # O texto é criptografado
        ciphertext = cipher.encrypt(padded_plaintext)
        
        #o texto criptografado é salvo em um arquivo de saída
        with open(output_file, 'wb') as f:
            f.write(ciphertext)
        
        #As chaves e o vetor de inicilização são salvos para serem usados no decrypt
        encoded_key = key.hex()
        encoded_iv = iv.hex()
        return encoded_key, encoded_iv
    except Exception as e:
        print(f"Ocorreu um erro ao tentar criptografar com o AES: {e}")
        return None, None