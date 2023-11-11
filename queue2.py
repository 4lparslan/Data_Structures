import queue

orders_queue = queue.SimpleQueue()

# Add elements
orders_queue.put("Sushi")
orders_queue.put("Doner")
orders_queue.put("Kebab")

print("The size is : ", orders_queue.qsize())

# Remove elements
orders_queue.get()

print("Is empty: ", orders_queue.empty())