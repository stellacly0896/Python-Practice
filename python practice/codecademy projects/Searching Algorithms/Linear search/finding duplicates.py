"""
With a few changes to our code, we can modify linear search to solve more complex search problems.

Our linear search function, linear_search(), currently finds whether one given value exists in a list, returns the index of the first occurrence of the value in the list, and stops. But what if we wanted to find every occurrence of the target value in a list?

The following is a list of locations for your favorite music artist’s upcoming tour:

[“New York City”, “Los Angeles”, “Bangkok”, “Istanbul”, “London”, “New York City”, “Toronto”]
You want to know during which tour stops will your favorite artist be in “New York City”.

Using the linear search algorithm, you can find that New York City will be the first stop on their tour, but the algorithm will indicate that your favorite artist will return to NYC later in the tour.

In order to find all duplicates of a target value in a list, we modify the algorithm to match the following pseudocode:

# For each element in the searchList
    # if element equal target value then
        # Add its index to a list of occurrences
# if the list of occurrences is empty
   # raise ValueError
# otherwise
   # return the list occurrences

"""

# Search list and target value
tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "New York City"

#Linear Search Algorithm
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
    if matches:
      return matches
  raise ValueError("{0} not in list".format(target_value))

#Function call
tour_stops = linear_search(tour_locations, target_city)
print(tour_stops)
