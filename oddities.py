cases = int(input())
nums = []
for _ in range(cases):
    num = int(input())
    nums.append(num)
for num in nums:
    if(num % 2 == 0):
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")