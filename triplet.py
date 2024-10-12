def find_triplet(arr, k):
    length = len(arr)
    triplet = []

    for i in range(length-3):
        left = i + 1
        after_left = left +1
        right = length - 1

        while left < right:
            if arr[i] + arr[left] + arr[after_left] +arr[right] == k:
                triplet.append((arr[i], arr[left], arr[after_left], arr[right]))
            right -=1
    return triplet

if __name__ == '__main__':
    print(find_triplet([-3, 2, 0, -5, 1, 5,4,6,-9,6,99,0], 1))
