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
    #self.Node0 = Node(value)
    self.head = Node(value)
    self.length = 1

  def length(self):
    return self.length
    
  def addNode(self, new_value):
    current_node = self.head
    for i in range(1, self.length):
      current_node = current_node.next
    current_node.changeNext(Node(new_value))
    self.length += 1
  
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
        
  def __str__(self):
    list = []
    current_node = self.head
    for i in range(self.length):
      list.append(current_node.value)
      current_node = current_node.next
    return str(list)
    
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
    
  # Finds particular node in linked list given an index
  def findNode(self, index):  
    current_node = self.head
    i = 0
    while i < index:
      current_node = current_node.next
      i += 1
    return current_node
    
  def removeNodesByValue(self, value):
    for i in range(self.length)[::-1]:
      if self.findNode(i).value == value: self.removeNode(i)
      
ll = LinkedList(1)
print ll # 1
ll.addNode(1)
print ll #12
ll.addNode(1) 
print ll # 123
ll.addNode(1) #123
print ll
ll.addNode(1)
print ll
ll.removeNodesByValue(2)
print ll
print ll.length
