def sumPair(arr,target):
    l =0
    r =len(arr) - 1
    pairs = set()
    arr.sort()

    while (l < r):
        sum = arr[l] + arr[r]

        if (sum > target):
            r -= 1
        elif (sum < target):
            l += 1
        elif (sum  == target):
            pairs.add((arr[l],arr[r]))
            l += 1

    if len(pairs) != 0:
        return pairs
    else:
        return "No Pair Found"

if __name__ == '__main__': 
    target = 145
    given = [3,6,7,4,8,10,12,15]
    result = sumPair(given, target)
    print(result)
