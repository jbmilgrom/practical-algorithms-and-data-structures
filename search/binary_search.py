# Search for item by leveraging sorted order of input list
# binarySearch: 
#   1. locate mid point
#   2. if item equals midpoint, return True
#   3. if item is less than midpoint, throwout right, binarySearch(left)
#   4. if item is greater than midpoint, throwout left, bindarySearch(right)
#   5. if no items left, return False
def binary_search(sortedList, item):
  length = len(sortedList)
  if length == 0:
    return False
  def iterate(sortedList, item, start, finish):
    if start == finish:
      return item == sortedList[start]
    mid = start + (1 + finish - start) // 2
    marker = sortedList[mid]
    if item == marker:
      return True
    if item < marker:
      return iterate(sortedList, item, start, mid - 1)
    else:
      return iterate(sortedList, item, mid, finish)
  return iterate(sortedList, item, 0, length - 1)

# TEST

print binary_search([1,2,4,5], 2)
print binary_search([1,2,4,5], 3)
print binary_search([1,2,4,5], 4)
print binary_search([1,2,4,5], 5)
print binary_search([1,2,4,5,8], 5)
print binary_search([1,2,4,5, 8], 6)
print binary_search([1,2,4,5, 8], 8)



