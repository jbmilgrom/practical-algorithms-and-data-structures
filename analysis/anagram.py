# Determine whether s1 is an anagram of s2
# alg: 
#   1. Check if letter in s1 is in s2
#   2. if not, return false
#   3. else, checkoff letter from s2
#   4. return tru
def isAnagramIterative(s1, s2):
  if len(s1) != len(s2):
    return False

  checkedOff = list(s2)

  for char1 in s1:
    for i, char2 in enumerate(checkedOff):
      if char1 == char2:
        checkedOff[i] = None
        break
    else: # no break
      return False
  return True
      
print isAnagramIterative('hello', 'ellho')
print isAnagramIterative('hello', 'elvho')