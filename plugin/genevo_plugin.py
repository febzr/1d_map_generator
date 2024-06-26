import random

class mapWithGrade:
    def __init__(self, map):
        self.map = map
        self.grade = self.setGrade()

    def getGrade(self):
        return self.grade
    
    def getMap(self):
        return self.map
    
    def setGrade(self):
        self.grade = 0

        if self.map[0] <= 16:
            self.grade += 5
        for i in range(len(self.map)-1):
            if i+1:
                if (self.map[i] - self.map[i+1] == 0):
                    self.grade += 2.5
                if (self.map[i] - self.map[i+1] == 1):
                    self.grade += 2
                if (self.map[i] - self.map[i+1] > 2):
                    self.grade += 3
                if (self.map[i] - self.map[i+1] == -1):
                    self.grade += 2
                if (self.map[i] - self.map[i+1] < -1):
                    self.grade -= abs(self.map[i] - self.map[i+1])

                if i >= 2 and (self.map[i] == 0):
                    if (self.map[i-1] - self.map[i+1] == 0):
                        self.grade -= 1
                    if (self.map[i-1] - self.map[i+1] == 1):
                        self.grade += 3
                    if (self.map[i-1] - self.map[i+1] > 2):
                        self.grade += 2
                    if (self.map[i-1] - self.map[i+1] == -1):
                        self.grade += 3
                    if (self.map[i-1] - self.map[i+1] < -1):
                        self.grade -= abs(self.map[i-1] - self.map[i+1])

        self.grade += max(self.map) - min(self.map)

        if self.grade > 0:
            self.grade = self.grade / len(self.map)

        return self.grade
    
    def setMap(self, map):
        self.map = map
        self.grade = self.setGrade()
    
def mutationMap(mapA, mapB, size):
    randomChoice = random.randint(0, 1)

    if randomChoice == 0:
        mapC = mapA.getMap()
        mapD = mapB.getMap()
        randomCut = random.randint(0, size)

        mapFinal = mapC[0:randomCut] + mapD[randomCut:size]

        return mapFinal
    
    if randomChoice == 1:
        mapC = mapB.getMap()
        mapD = mapA.getMap()
        randomCut = random.randint(0, size)

        mapFinal = mapD[0:randomCut] + mapC[randomCut:size]

        return mapFinal

def evolveProcess(mapA, mapB, mapC, mapD, mapE):
    mapList = [mapA, mapB, mapC, mapD, mapE]
    mapList.sort(key=lambda x: x.getGrade(), reverse=True)

    mapList[-1].setMap(mutationMap(mapList[0], mapList[1], sizeOfMap))

def finalizationCheck(mapA, mapB, mapC, mapD, mapE):
    mapList = [mapA, mapB, mapC, mapD, mapE]
    mapList.sort(key=lambda x: x.getGrade(), reverse=True)
    ifcounter = 0

    finalizermap = mapList[0].getMap()

    for i in range(len(finalizermap)-1):
        if finalizermap[i] - finalizermap[i+1] >= 0:
            ifcounter += 1
        if finalizermap[i] - finalizermap[i+1] == -1:
            ifcounter += 1

    if ifcounter == (len(finalizermap) - 1):
        return True
    
def plotMap(map):
    for i in range(20, 0, -1):
        for j in range(len(map)):
            if map[j] >= i:
                print("##", end="")
            else:
                print("  ", end="")
        print("\n")

def genevo(size):
    global sizeOfMap
    sizeOfMap = size
    counter = 0
    mutationCounter = 0
    finalizationCounter = 0
    stationCounter = 0
    check = False

    a = mapWithGrade([random.randint(0, 16) for _ in range(sizeOfMap)])
    b = mapWithGrade([random.randint(0, 16) for _ in range(sizeOfMap)])
    c = mapWithGrade([random.randint(0, 16) for _ in range(sizeOfMap)])
    d = mapWithGrade([random.randint(0, 16) for _ in range(sizeOfMap)])
    e = mapWithGrade([random.randint(0, 16) for _ in range(sizeOfMap)])

    while True:
        counter += 1
        mutationCounter += 1
        finalizationCounter += 1

        evolveProcess(a, b, c, d, e)

        if mutationCounter == 2:
            randomChoice = random.randint(0, 3)
            if randomChoice == 0:
                mapfromA = a.getMap()
                mapfromA[random.randint(0, sizeOfMap-1)] = random.randint(0, 20)
                a.setMap(mapfromA)
            if randomChoice == 1:
                mapfromB = b.getMap()
                mapfromB[random.randint(0, sizeOfMap-1)] = random.randint(0, 20)
                b.setMap(mapfromB)
            if randomChoice == 2:
                mapfromC = c.getMap()
                mapfromC[random.randint(0, sizeOfMap-1)] = random.randint(0, 20)
                c.setMap(mapfromC)
            if randomChoice == 3:
                mapfromD = d.getMap()
                mapfromD[random.randint(0, sizeOfMap-1)] = random.randint(0, 20)
                d.setMap(mapfromD)
            mutationCounter = 0

        if finalizationCounter == 5:
            
            if (a.getMap() == b.getMap() == c.getMap() == d.getMap() == e.getMap()) and (a.getGrade() == b.getGrade() == c.getGrade() == d.getGrade() == e.getGrade()):
                check = finalizationCheck(a, b, c, d, e)

            if check == True:
                objectList = [a, b, c, d, e]
                objectList.sort(key=lambda x: x.getGrade(), reverse=True)
                return objectList[0].getMap()

            finalizationCounter = 0