def check_palindrome(string, left,right):

    if left >= right:
        return True

    if left <= right and string[left] == string[right]:
        return check_palindrome(string, left+1, right-1)
    else:
        return False

def run(string):
    return check_palindrome(string, 0, len(string)-1)


def check_palindrome2(string):
    if string == "" or len(string) <=1:
        return True
    
    length = len(string) // 2
    for i in range(0,length,1):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

if __name__ == '__main__':
    print(check_palindrome2("ennnme"))
