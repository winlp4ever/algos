def minMoves(nums):
    n = len(nums)
    arr = sorted(nums)
    arr = [u - arr[0] for u in arr]
    print(arr)
    ds = [sum(arr)]
    for i in range(n-1):
        d = arr[i+1]-arr[i]
        ds.append(ds[-1] + (2*i+2-n)*d)
    return min(ds)

if __name__ == '__main__':
    a = [1,0,0,8,6]
    minMoves(a)