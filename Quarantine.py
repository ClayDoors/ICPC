start = input()
x = start.split()
numFriends = int(x[0])
daysUntil = int(x[2])
birthday = int(x[1])
birthday = birthday + daysUntil
friends = []
for i in range(numFriends):
    friends.append(int(input()))
counter = 0
for friend in friends:
    if friend+14 <= birthday:
        counter = counter + 1
print(counter)