"""
In order to test a product, many companies use empty or “fake” data. Our company, Searchcademy, uses empty sparsely sorted data to test its awesome search engine. What exactly does that mean? Sparsely Sorted Data is data such that there is empty data in between the sorted values. For instance, an example dataset might look like:

["Arthur", "", "", "", "", "Devan", "", "", "Elise", "", "", "", "Gary", "", "", "Mimi", "", "", "Parth", "", "", "", "Zachary"]
In this project, we will implement a modified version of iterative binary search to search through a sparsely sorted dataset.
"""

def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))

  first = 0
  last = len(data) - 1


  while first <= last:
    mid = (first+last)//2
    if not data[mid]:
      left = mid - 1
      right = mid + 1
      #handle empty data
      while True:
        if left < first or right > last:
          print ("{0} is not in the dataset".format(search_val))
          return
        elif right <= last and data[right]:
          mid = right
          break
        elif left >= first and data[left]:
          mid = left
          break
        else:
          right += 1
          left -= 1

    if data[mid] == search_val:
      print("{0} found at position {1}".format(search_val,mid))
      return

    if data[mid] > search_val:
      last = mid - 1

    if data[mid] < search_val:
      first = mid + 1


  print("{0} is not in the dataset".format(search_val))
