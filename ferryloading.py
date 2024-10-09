numTests = int(input())
trips = []
for _ in range(numTests):
    infoArr = input().split()
    ferryLen = int(infoArr[0])*100
    numCars = int(infoArr[1])
    leftCars = []
    rightCars = []
    for _ in range(numCars):
        carArr = input().split()
        if carArr[1] == "left":
            leftCars.append(int(carArr[0]))
        else:
            rightCars.append(int(carArr[0]))
    counter = 0
    if not leftCars:
        counter = 1
    while leftCars or rightCars:
        tripLen = ferryLen
        leftTrip = False
        rightTrip = False
        while leftCars and tripLen >= leftCars[-1]:
            tripLen -= leftCars.pop()
            leftTrip = True
        tripLen = ferryLen
        while rightCars and tripLen >= rightCars[-1]:
            tripLen -= rightCars.pop()
            rightTrip = True
        if leftTrip or rightTrip:
            counter += 2
        if (leftTrip ^ rightTrip) and not (rightCars or leftCars):
            counter -= 1
    trips.append(counter)
print(trips)



        
