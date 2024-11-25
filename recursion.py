#write a recursive function that will sum all digits of a number
def sumDigits(n):
    lastDigit = n %10
    remainder = n // 10
    if remainder == 0:
        return lastDigit
    return sumDigits(remainder) + lastDigit
print(sumDigits(0x123456789a))
def printRecursiveTriangle(n):
    if n == 1:
        print("1")
        return
    for i in range(n):
        print(i+1, end = " ")
    print()
    printRecursiveTriangle(n-1)
    for i in range(n):
        print(i+1, end = " ")
        
    print("")
printRecursiveTriangle(5)

def isPalidrone(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and isPalidrone(s[1:-2])