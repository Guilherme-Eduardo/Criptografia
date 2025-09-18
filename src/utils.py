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
    print ("*"*80)
    print (f"Nome do algoritmo: {name}")
    print (type)
    print(f"Tempo decorrido: {totalTime:.6f} segundos\n")
    

#Função de escrita dos valores
def write ():
    return True

#Função para plotar graficos para o relatório