import queue

my_book_stack = queue.LifoQueue(maxsize = 0) # maxsize = 0 means infinite

# push method
my_book_stack.put("Hello")
my_book_stack.put("Guys")
my_book_stack.put("What's up?")

print("The size is : ", my_book_stack.qsize())

# pop method
my_book_stack.get()

print("Is empty: ", my_book_stack.empty())