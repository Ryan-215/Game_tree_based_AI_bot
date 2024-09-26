class Stack: 
	def __init__(self, cap = 10):
		self.cap = cap
		self.stack_list = [None] * self.cap
		self.num_of_elem = 0

	def capacity(self):
		return self.cap

	def resize_grow(self):
		self.stack_list = self.stack_list + [None] * self.cap
		# update current capacity
		self.cap *= 2

	def resize_shrink(self):
		self.stack_list = self.stack_list[:self.num_of_elem]
		self.cap //= 2

	def push(self, data):
		# if push None, do nothing
		if data is not None:
			# if list if full, grow the capacity
			if self.cap == self.num_of_elem: # 1,2,3,4,5 cap = 5, numElem = 5
				self.resize_grow()
			self.stack_list[self.num_of_elem] = data
			self.num_of_elem += 1

	def pop(self):
		# pop nothing if list is empty
		if self.num_of_elem != 0:
			self.top_on_stack = self.stack_list[self.num_of_elem - 1]
			self.stack_list[self.num_of_elem - 1] = None
			self.num_of_elem -= 1
			# # shrink if nums of elem is half of cap
			# if self.cap > 10 and self.num_of_elem <= self.cap // 2:
			# 	self.resize_shrink()
			return self.top_on_stack
		else:
			raise IndexError('pop() used on empty stack')

	def get_top(self):
		if not self.is_empty():
			return self.stack_list[self.num_of_elem - 1]

	def is_empty(self):
		return self.num_of_elem == 0

	def __len__(self):
		return self.num_of_elem

class Queue:
	def __init__(self, cap = 10):
		self.cap = cap
		self.queue = [None] * self.cap
		self.num_of_elem = 0
		self.front = 0
		self.back = 0

	def capacity(self):
		return self.cap

	def resize_grow(self):
		# resize the list
		temp_queue = [None] * self.cap * 2
		for i in range(self.num_of_elem):
			temp_queue[i] = self.queue[(self.front + i) % self.cap]
		self.queue = temp_queue

		# update cap
		self.cap *= 2
		# reset front and back
		self.front = 0
		self.back = self.num_of_elem

	def enqueue(self, data):
		if data is not None:
			# check if resize needed
			if self.num_of_elem == self.cap:
				self.resize_grow()
			# calculate the back index to insert, circular maybe
			self.back = self.back % self.cap
			# assign data at the last blank
			self.queue[self.back] = data
			# update the back index and the number of elems in queue
			self.back += 1
			self.num_of_elem += 1

	def dequeue(self):
		if not self.is_empty():
			front_in_queue = self.queue[self.front]
			self.queue[self.front] = None
			self.num_of_elem -= 1
			self.front = (self.front + 1) % self.cap
			return front_in_queue
		else:
			raise IndexError('dequeue() used on empty queue')

	def get_front(self):
		if not self.is_empty():
			return self.queue[self.front]

	def is_empty(self):
		return self.num_of_elem == 0

	def __len__(self):
		return self.num_of_elem



class Deque: 
	def __init__(self, cap = 10):
		self.cap = cap
		self.deque = [None] * self.cap
		self.num_of_elem = 0
		self.front = 0
		self.back = 1

	def capacity(self):
		return self.cap

	def resize_grow(self):
		temp_deque = [None] * self.cap * 2
		for i in range(self.num_of_elem):
			temp_deque[i] = self.deque[(self.front + 1 + i) % self.cap]
		self.deque = temp_deque
		self.cap *= 2
		self.front = self.cap - 1
		self.back = self.num_of_elem

	def push_front(self, data):
		if data is not None:
			if self.cap == self.num_of_elem:
				self.resize_grow()
			self.front = self.front % self.cap
			self.deque[self.front] = data
			self.front -= 1
			self.num_of_elem += 1

	def push_back(self, data):
		if data is not None:
			if self.cap == self.num_of_elem:
				self.resize_grow()
			self.back = self.back % self.cap
			self.deque[self.back] = data
			self.back += 1
			self.num_of_elem += 1

	def pop_front(self):
		if not self.is_empty():
			# change to the current front value position
			self.front = (self.front + 1) % self.cap
			# remove data
			front_in_deque = self.deque[self.front]
			self.deque[self.front] = None
			# modify deque info
			self.num_of_elem -= 1

			return front_in_deque
		else:
			raise IndexError('pop_front() used on empty deque')

	def pop_back(self):
		if not self.is_empty():
			# change to the current back value position
			self.back = (self.back - 1) % self.cap
			# remove data
			back_in_deque = self.deque[self.back]
			self.deque[self.back] = None
			# modify deque info
			self.num_of_elem -= 1

			return back_in_deque
		else:
			raise IndexError('pop_back() used on empty deque')

	def get_front(self):
		return self.deque[(self.front + 1) % self.cap]

	def get_back(self):
		return self.deque[(self.back - 1) % self.cap]

	def is_empty(self):
		return self.num_of_elem == 0

	def __len__(self):
		return self.num_of_elem

	def __getitem__(self, k):
		if k < 0 or k >= self.num_of_elem:
			raise IndexError('Index out of range')
		else:
			return self.deque[(self.front + 1 + k) % self.cap]
