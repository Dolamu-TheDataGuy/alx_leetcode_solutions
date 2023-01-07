#!/usr/bin/python3
def compare_func(str, first, last):
        if len(str) == 1:
            return True
        if not str[first].isalnum():
            first = first + 1
        if not str[last].isalnum():
            last = last - 1
        if str[first].lower() == str[last].lower():
          if first == last or first == last + 1:
            return True
          else:
            return compare_func(str, first + 1, last - 1)
        else:
          return False

def verify_palidrome(str):
  return compare_func(str, 0, (len(str) - 1))

def for_verify(str):
  temp = ''
  for x in str:
    if x.isalnum():
      temp = temp + x.islower()
  return temp
if __name__ == "__main__":
  print(verify_palidrome(' '))
  