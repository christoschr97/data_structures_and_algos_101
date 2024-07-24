from data_structures.linked_list.linked_list import LinkedList

my_list = LinkedList(5)
my_list.insert_beginning(10)
my_list.insert_beginning(15)

print(my_list.stringify_list())

my_list.remove_node(10)

print(my_list.stringify_list())