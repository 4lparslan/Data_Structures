def linear_search(unordered_list, search_value):
	for index in range(len(unordered_list)):
		if unordered_list[index] == search_value:
			return True
	return False