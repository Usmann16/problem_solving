# (((({{[]}}))l)l)

def valid_paranthesis(s:str) -> bool:
    if len(s) == 0:
        return True

    valided_list = []
    for i in s:
        if i == '(':
            valided_list.append(i)
        elif i == '{':
            valided_list.append(i)
        elif i == '[':
            valided_list.append(i)

        else:
            if i == ')':
                if valided_list and valided_list[-1] == '(':
                    valided_list.pop()
                else:
                    return False

            if i == '}':
                if valided_list and valided_list[-1] == '{':
                    valided_list.pop()
                else:
                    return False

            if i == '[':
                if valided_list and valided_list.get[-1] == ']':
                    valided_list.pop()
                else:
                    return False

    return len(valided_list) == 0


if __name__ == '__main__':
    print(valid_paranthesis('{()})'))