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
        matrix.extend(line)
    
    print("Matriz inicial:")
    printMatrix(matrix)
    return matrix    
    
    
# Faz a transposição entre o primeiro, ultimo e o valor do ultimo elemento na tab. ASCII    
def transposition(matrix):
    #Pega o primeiro elemento
    first = matrix[0]
    
    #Guarda o ultima caracter da 1° linha e pega o seu valor na tabela ASCII
    lineLastChar = matrix[4]
    valueLastChar = ord(lineLastChar)   #Valor na Tab. ASCII
    digits = str(valueLastChar)         #Somo os Digitos
    sum_digits = sum(int(d) for d in digits)
    print ("\nFazendo a transposição...\n"
           "Soma do ultimo digito da 1° da linha da tab. ASCII: ", sum_digits)
    
    #Transposição (Triângulo de Guilherme)
    matrix[0] = lineLastChar
    matrix[4] = matrix[sum_digits - 1]
    matrix[sum_digits - 1] = first  
    return matrix
    
    
def printMatrix(matrix):
    for i in range(0, 25, 5):
        line = matrix[i:i+5]
        print(line)
        
        
def encryptPlayfair(matrix, text):
    return

    """
    while(!EOF()){
        
    }
    """
    
    
def encryptCesar(text, value):
    return True
    
    

def encryptAES():
    return True

    
printMatrix(transposition(createPlayfairMatrix("HELOISA")))
    
    
    
    