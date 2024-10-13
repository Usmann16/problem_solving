# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def arrange_anagrams(arr: list) -> list:
    result = {}
    for s in arr:
        sort_s = ''.join(sorted(s))
        if result.get(sort_s):
            result[sort_s] = [*result.get(sort_s), s]
        else:
            result[sort_s] = [s]
    return list(result.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(arrange_anagrams(strs))
