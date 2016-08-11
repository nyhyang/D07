# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()
from itertools import accumulate

def cumulative_sum(nested_lst):
	# cumulative_lst = [itertools.accumulate(item) for item in nested_lst]
	cumulative_lst = [list(accumulate(lst)) for lst in nested_lst]
	return cumulative_lst


	# cumulative_lst = []
	# for lst in nested_lst:
	# 	for item in lst:

	# for item in nested_lst:
	# 	cumulative_lst += itertools.accumulate(item)
	# return cumulative_lst









def main():
	cumulative_sum(([1, 2, 4], [2, 3, 4]))

if __name__ == '__main__':
	main()


