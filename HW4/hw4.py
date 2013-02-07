class Node(object):
  def __init__(self, _value = None, _next = ''):
    self.value = _value
    self.next = _next
  
  def __str__(self):
    return str(self.value)

  def changeNext(self, new_next):
    self.next = new_next
    
class LinkedList(object):
  def __init__(self, value):
    self.head = Node(value)
    self.length = 1

  def length(self):
    return self.length
    
  def __str__(self):
    list = []
    for i in range(self.length):
      list.append(self.findNode(i).value)
    return str(list)
    
  # Finds particular node in linked list given an index
  def findNode(self, index):  
    current_node = self.head
    i = 0
    while i < index:
      current_node = current_node.next
      i += 1
    return current_node
    
  def addNode(self, new_value):
    if self.length == 0: self.__init__(new_value)
    else:
      current_node = self.head
      for i in range(1, self.length):
        current_node = current_node.next
      current_node.changeNext(Node(new_value))
      self.length += 1
  
  # Checks whether a given index exists in the list
  def checkIndex(self, index):
    if index not in range(self.length): raise Exception, "No node at this location."
    
  def removeNode(self, node_to_remove):
    self.checkIndex(node_to_remove)
    PriorNode = self.findNode(node_to_remove-1)
    NodeToRemove = self.findNode(node_to_remove)
    if NodeToRemove == self.head:
      self.head = self.head.next
    else:
      PriorNode.changeNext(PriorNode.next.next)
    self.length -= 1
    
  def addNodeAfter(self, new_value, after_node):
    self.checkIndex(after_node)
    NodeToAppend = self.findNode(after_node)
    NodeToAppend.changeNext(Node(new_value, NodeToAppend.next))
    self.length += 1
    
  def addNodeBefore(self, new_value, before_node):
    self.checkIndex(before_node)
    if before_node == 0: 
      self.head = Node(new_value, self.head)
    else:
      PriorNode = self.findNode(before_node-1)
      PriorNode.changeNext(Node(new_value, PriorNode.next))
    self.length +=1
    
  def removeNodesByValue(self, value):
    for i in range(self.length)[::-1]:
      if self.findNode(i).value == value: self.removeNode(i)
      
  def reverse(self):
    for i in range(self.length)[::-1]:
      self.addNode(self.findNode(i).value)
    for i in range(self.length/2):
      self.removeNode(0)
    
ll = LinkedList(0)
print ll # 1
ll.addNode(0)
print ll
ll.addNode(1)
print ll #12
ll.addNode(2) 
print ll # 123
ll.addNode(3) #123
print ll
print ll.head.next.next
ll.head.next.next.changeNext(ll.head)
print ll

