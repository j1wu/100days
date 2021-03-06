import doctest

def uni_char(s):
  """
  Created on 2017-06-07 11:12:05
  Author: Ji Wu

  Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

  >>> uni_char('')
  True
  >>> uni_char('goo')
  False
  >>> uni_char('abcdefg')
  True
  """
  if len(s) == 1:
    return True

  return len(list(s)) == len(set(s))


if __name__ == '__main__':
  doctest.testmod()