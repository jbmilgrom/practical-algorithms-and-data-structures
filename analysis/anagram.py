# Determine whether s1 is an anagram of s2
# alg: 
#   1. Check if letter in s1 is in s2
#   2. if not, return false
#   3. else, checkoff letter from s2
#   4. return tru
def is_anagram_checking_off(s1, s2):
  if len(s1) != len(s2):
    return False

  checked_off = list(s2)

  for char1 in s1:
    for i, char2 in enumerate(checked_off):
      if char1 == char2:
        checked_off[i] = None
        break
    else: # no break
      return False
  return True
      
print is_anagram_checking_off('hello', 'ellho')
print is_anagram_checking_off('hello', 'elvho')
