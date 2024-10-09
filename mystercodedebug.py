
def subset_sum(numbers, target, flag=[], results=[], longest=[]):
    s = sum(flag)
    if s == target:
        results.append(flag.copy())
        if len(flag) > len(longest):
            longest[:] = flag
    if s >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, flag + [n], results, longest)
        
    return longest

def truesubset_sum(numbers, target, flag=[], results=[], longest=[]):
    s = sum(flag)
    if s == target:
        results.append(flag.copy())
        if len(flag) > len(longest):
            longest[:] = flag
    if s >= target:
        return
    for i in range(len(numbers)):
        n = numbers[i]
        print(flag)
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, flag + [n], results, longest)
        
    return longest
truesubset_sum([1,1,1,2,2,3,4,4,5,5,6,7,8],13)