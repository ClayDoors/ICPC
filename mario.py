inputs = int(input())
goombas = []
rooms = []
for i in range(inputs):
    nums = input().split()
    goombas.append(int(nums[0]))
    rooms.append(int(nums[1]))
goombaCounter = 0
for i in range(inputs):
    goombaCounter += goombas[i]
    if goombaCounter < rooms[i]:
        print('impossible')
        exit()
print('possible')