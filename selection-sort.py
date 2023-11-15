def selectionSort(arr):
	size = len(arr)
	for i in range(size):
		min_idx = i

		for j in range (i+1, size):
			if arr[j] < arr[min_idx]:
				min_idx = j

		# swapping the values
		arr[min_idx], arr[i] = arr[i], arr[min_idx]

data = [-2, 15, 6, 48, -12, 23, 25, 5]
selectionSort(data)
print(data)