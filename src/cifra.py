# Trabalho 1 realizado por Guilherme Eduardo & Heloisa Pinho
# GRR20231950 & GRR20231961
# Disciplina: Criptografia


def readFile():
    return True


def formatFile():
    return True


# Cria a matriz de play fair inicial
def createPlayfairMatrix(key):
    #Concateno o alfabeto na chave
    key = key.replace('J', 'I').upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    # Remove letras repetidas
    key = "".join(dict.fromkeys(key))
    
    matrix = []
    # i vai ser 0, 5, 10, 15, 20 -> e incrementa os valores na matriz
    for i in range(0, 25, 5):
        line = []
        for k in key[i:i+5]:
            line.append(k)
        matrix.append(line)
    
    print("Matriz inicial:")
    printMatrix(matrix)
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

    print ("\nFazendo a transposição...\n"
           "Soma do ultimo digito da 1° da linha da tab. ASCII: ", sum_digits)
    
    #Transposição (Triângulo de Guilherme)
    matrix[0][0] = lineLastChar
    matrix[0][4] = matrix[line][column]
    matrix[line][column] = first  
    return matrix
    
    
def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[i])):
            print (matrix[i][j], end=" ")
        print ("")

# Encontra as posições de linha e coluna da respectiva Letra na matriz playfair
def findPositionMatrix(matrix, char):
    line = 0
    column = 0
    for i in range (0, len(matrix)):        
        for j in range (0, len(matrix[i])):
            if (char == matrix[i][j]):
                line = i
                column = j
                return line, column

    return 0


# Responsavel por fazer as substituções na cifra
def playfairSubstitutionEnc(matrix, line1, line2, column1, column2):
    char1 = char2 = 0

    #Letras na mesma linha
    if line1 == line2:
        char1 = 0 if column1 % 5 == 1 else column1 + 1
        char2 = 0 if column1 % 5 == 1 else column2 + 1
        return matrix[line1][char1], matrix[line2][char2]
    
    #Letras na mesma coluna
    elif column1 == column2:
        char1 = 0 if column1 % 5 == 1 else line1 + 1
        char2 = 0 if column1 % 5 == 1 else line2 + 1
        return matrix[char1][column1], matrix[char2][column2]

    else:
        return matrix[line1][column2], matrix[line2][column1]

        
def playfairEncript(matrix, text, key):
    #Cria a matriz e já faz a transposição
    matrix = createPlayfairMatrix(key)
    matrix = transposition(matrix)
    encryptedText = []

    #Adiciona a letra "X" caso no final do arquivo seja impar
    if len(text) % 2 == 1:
        text += 'X'
    
    for i in range (0, len(text), 2):
        #Pega um par de letras
        pairLetters = text[i:i+2]

        #Localiza as coordenadas na matriz para a respectiva letra/caracter
        line1, column1 = findPositionMatrix (matrix, pairLetters[0])
        line2, column2 = findPositionMatrix (matrix, pairLetters[1])

        #Faz a substituição conforme a cifra de playfair
        encryptedText.extend(playfairSubstitutionEnc(matrix, line1, line2, column1, column2))

    print (encryptedText)
    
def cesarEncrypt(text, value):
    return True
    
    

def aesEncrypt():
    return True

    

phrase = "CRIPTOGRAFIA"
playfairEncript(m, phrase, "HELOISA")


    
    
    
    