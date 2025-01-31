"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1


def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO
	# if the key can not be found in the tree then it will return -1 
	if left > right:
		return -1
	# find the middle of the binary search tree 
	middle = (left + right) // 2
		# if the key is in the middle, return that index 
	if mylist[middle] == key:
		return middle
		# if the key is less than the value that is in the middle of the tree, then search the left side of the tree 
	elif mylist[middle] > key:
		return _binary_search(mylist, key, left, middle - 1)
		# if the key is greater than the value that is in the middle of the tree, then search the right side 
	else:
		return _binary_search(mylist, key, middle + 1, right)
	###




def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `search_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	# get the sart time
	start = time.time()
	# runs the function
	search_fn(mylist, key)
	# get the end time 
	end = time.time()
	# by subtracting the start time by the end time, it gets the total time the search function took to run
	# multiply the time by 1000 to convert to milliseconds
	return (end - start) * 1000
	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	# create an empty list that will be used to store the results 
	mylist=[]
	# use a for loop to go through the list of sizes
	for size in sizes:
		# create a list of numbers to use as input for linear search and binary search
		arr = list(range(int(size))) 
		# get the run time for linear search
		linear_search_time = time_search(linear_search, arr, -1)
		# get the run time for the binary search 
		binary_search_time = time_search(binary_search, arr, -1)
		# append the results to the list 
		mylist.append((size, linear_search_time, binary_search_time))

	# return the appended list that was created 
	return mylist
	###

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

# call print_results to print the results from compare_search
print_results(compare_search())
