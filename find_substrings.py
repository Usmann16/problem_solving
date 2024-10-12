def find_substrings(string, k):
    if len(string) < k:
        return []
    current = string
    hashset = {}
    result = []
    for i in range(len(string)-k):
        substring = current[i:i+k]
        if substring not in hashset:
            hashset[substring] = 0
        else:
            hashset[substring] +=1
        current = string
    
    if hashset:
        for k, v in hashset.items():
            if v > 0:
                result.append(k)
    return result




if __name__ == '__main__':
    print(find_substrings("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", 10))