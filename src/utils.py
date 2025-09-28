import re

def formatFile(cleanText):
    cleanText = cleanText.upper().replace("J", "I")     # Substitui o J por I
    cleanText = re.sub(r"[^A-Z0-9]", "", cleanText)     # Mantém apenas letras A–Z e números
    return cleanText


def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[i])):
            print (matrix[i][j], end=" ")
        print ("")
        
        
#Retorna as informações sobre tempo de duraçao da cifra/decifra
def timeEvaluation(name, type, initTime, endTime):
    totalTime = endTime - initTime
    resultado = (
        f"\nAvaliação da {type}\n"
        f"Nome do algoritmo: {name}\n"
        f"Tempo decorrido: {totalTime:.6f} segundos\n"
        + "*"*80 + "\n"
    )
    print(resultado)   # continua mostrando no console
    return resultado   # mas também devolve como string


#Função de escrita dos valores
def write ():
    return True

#Função para plotar graficos para o relatório