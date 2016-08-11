# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def is_sorted(nested_lst):
	
	sorted_lst = []
	for lsts in nested_lst:
		try:
			sorted_lst = sorted(lsts)
		except:
			print("It's not sortable. ")

		if lsts == sorted_lst:
			return True
		else:
			return False




def main():

	# print(is_sorted(([1, 2, 3], [2, 3, 4])))
	# print(is_sorted(["b", "a", "c"]), [1, 2, 3])
	# print(is_sorted(['a', 'b', 'c'] [1, 2, 3]))

	is_sorted(nested_lst)

if __name__ == '__main__':
	main()
