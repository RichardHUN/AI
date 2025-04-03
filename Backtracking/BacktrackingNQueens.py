#f = open("output.txt", "w")

def generateMatrix(nrOfRows, nrOfCols, value = 0):
    """Adott méretű, egy adott értékkel feltöltött mátrixot gyárt"""
    return [[value for x in range(nrOfCols)] for x in range(nrOfRows)]

def matrixPrinter2D(matrix, descr = None):
    """Soronként írja ki a mátrixot, opcinálisan elé egy megjegyzést"""
    #tesztelésre használtam
    if descr is not None:
        print(descr)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end= " ")
        print("\n")

"""
def matrixPrinter2DFile(matrix, descr = None):
    #Soronként írja ki, tesztelésre használtam
    if descr is not None:
        print(descr, file = f)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end= " ", file = f)
        print("\n", file=f)
"""

def countOnesInMatrix(table):
    cnt = 0
    for row in table:
        for elem in row:
            if elem == 1:
                cnt += 1
    return cnt

def generateAvailabilityMatrixForGivenElement(nrOfRows, nrOfCols, rowIndex, columnIndex):
    """
    Legyárt egy elérhetőség mátrixot egy adott elemnek;
    (0<-szabad/1<-nem szabad)
    """
    #1-es lett az ütés a későbbi logikai vagyozás miatt

    availabilityMatrix = generateMatrix(nrOfRows, nrOfCols, 0)
    for i in range(nrOfRows):
        for j in range(nrOfCols):
            #Ha ugyan abban a sorban vagy oszlopban vannak
            #                                    vagy ugyan azon az átlón vannak
            if i == rowIndex or j == columnIndex or i + j == rowIndex + columnIndex or i - j == rowIndex - columnIndex:
                #Akkor az adott helyre már nem lehet rakni
                availabilityMatrix[i][j] = 1
    return availabilityMatrix
"""
#mátrix-generálás teszt(elemenként)
aM00 = generateAvailabilityMatrix(4, 4, 0, 0)
matrixPrinter2D(aM00, "(0,0)")

aM22 = generateAvailabilityMatrix(4, 4, 2, 2)
matrixPrinter2D(aM22, "(2,2)")
"""
"""
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33
"""

def generateFullAvailabilityMatrix(size):
    """Legyártja a teljes elérhetőség mátrixot;
    Egy 4x4-es mátrix (pl i és j indexekkel),
    melynek minden eleme egy 4x4-es mátrix (pl m és n indexekkel), amely azt tárolja,
    hogy ha az adott helyre (i,j) rakunk egy királynőt, hova rakhatunk a továbbiakban (m, n),
    (0-szabad, 1-ütés(nem szabad))"""
    availabilityMatrix = [[generateAvailabilityMatrixForGivenElement(size, size, i, j) for i in range(size)] for j in range(size)]
    return availabilityMatrix
"""
#teljes mátrix-generáláls teszt
aM = generateFullAvailabilityMatrix(4)
print(aM)
"""

def logicalOrForMatrix(M1, M2):
    """Két availabilityMatrix-ot kombinál"""
    M3 = generateMatrix(len(M1), len(M1), 0)
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            M3[i][j] = M1[i][j] or M2[i][j]
    return M3

def generateCurrentAvailabilityMatrix(table):
    """A megadott tábla állása szerint gyártja le az availabilityMatrix-ot(0-szabad/1-nem szabad)"""
    currentAvailabilityMatrix = generateMatrix(len(table), len(table[0]), 0)
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 1:
                currentAvailabilityMatrix = logicalOrForMatrix(currentAvailabilityMatrix, generateAvailabilityMatrixForGivenElement(len(table), len(table), i, j))
    return currentAvailabilityMatrix

# #Csak mintának van bent
# def backtracking_default(graph, graf_colors, v, colors, h=None):
#     """A graph_coloring_util függvény rekurzívan meghívja önmagát minden csúcsra és megpróbálja kiválasztani a színeket.
#     Ha egy adott szín nem biztonságos (azaz ha már használják egy szomszédos csúcson), akkor kipróbál egy másik színt.
#     Ha egyik szín sem biztonságos, akkor visszalép és megpróbálja újraszínezni az előző csúcsot."""
#
#     # Megvizsgáljuk hogy melyik elemnél vagyunk
#     # ha 'v' == a gráf hosszával akkor készen vagyunk
#     if v == len(graph):
#         return True
#
#     # Próbáljuk végig a szineket
#     for c in range(colors):
#         # Ha kiszinezhető a 'v' csúcs a 'c' színnel
#         if h(graph, graf_colors, v, c):
#
#             # színezzük ki a 'v' csúcsot 'c' színnel
#             graf_colors[v] = c
#
#             # szinezzük ki a következő csúcsot
#             if backtracking_default(graph, graf_colors, v + 1, colors, h):
#                 return True
#
#             # ha nem sikerül visszalépünk és az aktuálisan
#             # kiszinezett csúcsot '-1'-re azaz szín nélkülire állítjuk
#             graf_colors[v] = -1
#
#     return False

def backtracking(table, rowIndex, columnIndex, eval):
    #Emlékeztető: availabilityMatrix: 1-ütés, 0-szabad
    #             table: 1-királynő, 0-semmi

    currentAvailabilityMatrix = generateCurrentAvailabilityMatrix(table)
    nrOfQueens = countOnesInMatrix(table)

    if rowIndex == len(table):
        if nrOfQueens == 4:
            return True
        return False

    #Előbb királynőt probál meg rakni, majd ha nem sikerül, akkor semmit
    queens = [i for i in range(2)]
    queens.reverse()
    for queen in queens:
        #Ha az adott helyre lerakható királynő
        if eval(table, currentAvailabilityMatrix , rowIndex, columnIndex, queen, nrOfQueens):
            #lerakja
            table[rowIndex][columnIndex] = queen

            #Ezzel teszteltem a kiíratás hosszát
            #matrixPrinter2DFile(table, "Tabla")

            #és próbálja folytatni tovább
            #ha sor végén van, akkor a következő sorba folytatja
            if columnIndex == len(table)-1:
                if backtracking(table, rowIndex+1, 0, eval):
                    return True
            else:
                if backtracking(table, rowIndex, columnIndex+1, eval):
                    return True

            #Ha nem megfelelő, -1-re állítja
            table[rowIndex][columnIndex] = -1
    return False


def availabilityTester(table, availabilityMatrix, rowIndex, columnIndex, queen, nrOfQueens):
    """Leteszteli, hogy az aktuális megszorítások szerint
    az adott helyre rakható-e az adott bábú
    (királynő<-1/semmi<-0)"""
    #Legbanálisabb
    #Ha nem akar semmit lerakni, akkor biztosan nem szabálytalan
    if queen == 0:
        return True

    #Ha királynő kerülne az adott helyre
    #Ha szabad királynőt rakni az adott helyre
    if availabilityMatrix[rowIndex][columnIndex] == 0:
        return True
    return False

def availabilityPlusEmptyRowsChecker(table, availabilityMatrix, rowIndex, columnIndex, queen, nrOfQueens):
    """Leteszteli, hogy az aktuális megszorítások szerint
    az adott helyre rakható-e az adott bábú + hogy nincs-e üres sor
    (királynő<-1/semmi<-0)"""

    #Ha a sor utolsó elemét vizsgáljuk
    #                       és épp nem akarnánk királynőt lerakni
    #                                                 és a sorba nem raktunk királynőt
    if columnIndex == len(table[0])-1 and queen == 0 and table[rowIndex].count(1) == 0:
        return False

    #Ha nem akar semmit lerakni, akkor biztosan nem szabálytalan
    if queen == 0:
        return True

    #Ha királynő kerülne az adott helyre
    #Ha szabad királynőt rakni az adott helyre
    if availabilityMatrix[rowIndex][columnIndex] == 0:
        return True
    return False


#Legyártom előre, hogy ne kelljen a backtracking közbe gyártogatni egyessével az availabilityMatrix-okat
fullAvailabilityMatrix = generateFullAvailabilityMatrix(4)

#Tábla inicializálása
table = generateMatrix(4,4, -1)

#746 sor a kiíratása az összes legenerált táblának
#print( backtracking(table, availabilityMatrix, 0, 0, availabilityTester))
print( backtracking(table, 0, 0, availabilityTester))
print( table )

#print("=======================================", file=f)

table = generateMatrix(4,4, -1)
availabilityMatrix = generateMatrix(4,4, 0)

#341 sor a kiíratása az összes legenerált táblának
print( backtracking(table, 0, 0, availabilityPlusEmptyRowsChecker))
print( table )

#f.close()