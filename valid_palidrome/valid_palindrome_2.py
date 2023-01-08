#!/usr/bin/py
def isPalindrome(self, s: str) -> bool:
        temp = ''
        for i in s:
            if i.isalnum():
                i = i.lower()
                temp += i
        if temp == temp[::-1]:
            return True
        return False