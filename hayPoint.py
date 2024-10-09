x = input().split()
keys = int(x[0])
paragraphs = int(x[1])
points = {}
for i in range(keys):
    line = input().split()
    points[line[0]] = int(line[1])
periodCount = 0
score = 0
scores = []
while paragraphs > periodCount:
    line = input().split()
    if "." in line:
        scores.append(score)
        score = 0
        periodCount += 1
    else:
        for word in line:
            if word in points:
                score += points[word]
for s in scores:
    print(str(s))
