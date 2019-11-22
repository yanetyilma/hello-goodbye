from linked_list import Node, Linked_list

class Stack(Linked_list):
	def __init__(self, head = None):
		super().__init__(head)
	def push(self, d):

		new_node = Node(data = d, next_node = self.head)

		self.head = new_node

		self.size +=1

	def pop(self, d):
		current_node = self.head

		next_node = current_node.get_next()

		self.head = next_node

		current_node.set_next(n = None)

		self.size -=1

		return(current_node.get_data())

def main():
	my_stack = Stack()

	my_stack.push(d = 100)
	my_stack.push(d = 1000)
	my_stack.push(d = "AU")
	my_stack.push(d = "GW")

	my_stack.search()
	
	# print(my_stack.pop())
	# print(my_stack.get_size())

if __name__ == '__main__':
	main()