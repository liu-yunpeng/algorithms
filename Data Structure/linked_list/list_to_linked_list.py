l1 = [2,4,3]
l2 = [5,6,4]


class Node(object):
	"""docstring for Node"""
	def __init__(self, value = None, next = None):
		super(Node, self).__init__()
		self.value = value
		self.next = next
		

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self, lst):
		self.head = Node('head')
		self.tail = Node()
		self.head.next = self.tail

		if not lst:
			return

		curr_node = self.head

		for i in lst:
			i_node = Node(i)
			curr_node.next = i_node
			curr_node = i_node

		curr_node.next = self.tail


	def print_values(self):
		curr_node = self.head.next

		while curr_node.value is not None:
			print(curr_node.value)
			curr_node = curr_node.next

l1_list = LinkedList(l1)
l2_list = LinkedList(l2)

l1_list.print_values()
l2_list.print_values()

