
def contains(list_1, list_2):
  a =0
  while True:
    if list_2 == list_1[a : a + len(list_2)]:
      return True
      break 
    else:
      a += 1
      if a + len(list_2) > len(list_1):
        return False
        break
        
list1 = [1, 6, 2, 1, 4, 1, 2, 1, 8]
list2 = [1, 2, 1]

print(contains(list1, list2))
