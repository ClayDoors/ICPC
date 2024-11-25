index = -1
biggest = -1
for i in range(5):
    nums = (input()).split()
    for j in range(4):
        nums[j] = int(nums[j])
    s = sum(nums)
    if s > biggest:
        biggest = s
        index = i+1
print(str(index)+" "+ str(biggest))