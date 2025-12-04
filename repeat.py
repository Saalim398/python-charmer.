#to find all the elements that appear n/3 times
a = [1,2,3,5,4,6,7,8,9,5,5,5,5]
def repat(nums):
    unique = []
    freq = []

    for x in nums:
        if x in unique:
            idx = unique.index(x)
            freq[idx]+=1
        else:
            unique.append(x)
            freq.append(1)

    n = len(nums)
    result = []
    for i in range(len(unique)):
        if freq[i]> n//3:
            result.append(unique[i])
    return result

print(repat(a))