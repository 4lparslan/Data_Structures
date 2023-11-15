def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(0, len(arr) - i - 1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp

data = [-2, 15, 6, 48, -12, 23, 25, 5]
bubbleSort(data)
print(data)