import queue

from WidthSearchTest.Csomopont import Csomopont

szomszedsag = [[0, 1, 1, 0, 0, 0],
               [0, 0, 1, 0, 1, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 1],
               [0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 0]]


hossz = [-1, -1, -1, -1, -1, -1]
szulo = [-1, -1, -1, -1, -1, -1]

def szelessegiKereses(szomszedsagiMatrix, kezdopont):
    hossz[kezdopont] = 0
    szulo[kezdopont] = -1
    sor = queue.Queue()
    sor.put(kezdopont)
    while not sor.empty():
        i = sor.get()
        for j in range(0, len(szomszedsagiMatrix[0])):
            if szomszedsagiMatrix[i][j] > 0:
                if hossz[j] == -1:
                    hossz[j] = hossz[i] + 1
                    szulo[j] = szulo[i] + 1
                    sor.put(j)

szelessegiKereses(szomszedsag, 0)
print(hossz)
print(szulo)