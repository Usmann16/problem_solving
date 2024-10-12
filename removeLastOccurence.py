# [0,4,2,5,4,7,5,5,0,8,9,0,4]

def removeLastOccurence(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    hashset = {}
    for i in range(len(arr)):
        if arr[i] not in hashset:
            hashset[arr[i]] = 0
        else:
            hashset[arr[i]] = i

    indexToRem = list(filter(lambda x:x!=0, hashset.values()))
    new_arr = [arr[i] for i in range(len(arr)) if i not in indexToRem]

    return list(new_arr)

if __name__ == '__main__':
    print(removeLastOccurence([0,4,2,5,4,7,5,5,0,8,9,0,4]))