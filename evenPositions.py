numTests = int(input())
tests = []
for _ in range(numTests):
    x = input()
    tests.append(list(input()))

for test in tests:
    counter = 0
    for i in range(1,len(test),2):
        
        if test[i] == "(":
            for j in range(i,len(test)):
                if test[j] == "_":
                    test[j] = ")"
                
                    counter += abs(i-j)
                    break
        elif test[i] == ")":
            for j in range(i-1,-1,-1):
                if test[j] == "_":
                    test[j] = "("
                    counter += abs(i-j)
                    break
    print(counter)