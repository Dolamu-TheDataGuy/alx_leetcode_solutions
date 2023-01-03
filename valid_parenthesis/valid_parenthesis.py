#!/usr/bin/python3
def valid_paren(s):
    """
    Given a string s containing just the characters 
    '(', ')', '{', '}', '[' and ']', determine if 
    the input string is valid.
    """
    left_par = ['(', '[', '{']
    right_par = [')', ']', '}']
    s_list = []
    if len(s) == 0 or len(s) % 2 != 0:
        return False
    for i in range(0, len(s)):
        if s[i] in left_par:
            idx = left_par.index(s[i])
            s_list.append(idx)
            print(s_list)
        elif s[i] in right_par:
            if (s_list[(len(s_list) - 1)] == right_par.index(s[i])) and (len(s_list) > 0):
                s_list.pop(s_list[len(s_list) -1])
            elif (len(s_list) == 0):
                return True
        else:
            return False

if __name__ == "__main__":
    print(valid_paren("{()}"))