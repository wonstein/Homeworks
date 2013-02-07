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
    #exec "self.Node%s = Node(new_value)" % self.length
    #exec "self.Node%s.changeNext(self.Node%s)" % (self.length-1, self.length)
    current_node = self.head
    for i in range(1, self.length):
      current_node = current_node.next
    current_node.changeNext(Node(new_value))
    self.length += 1
  
  def removeNode(self, node_to_remove):
    if node_to_remove >= self.length: raise Exception, "No node at this location."
    if node_to_remove == 0:
      self.head = self.head.next
    else:
      i = 1
      current_node = self.head
      while i < node_to_remove:
        current_node = current_node.next
        i += 1
      current_node.changeNext(current_node.next.next)
    self.length -= 1
        
    
  def __str__(self):
    list = []
    current_node = self.head
    for i in range(self.length):
      list.append(current_node.value)
      current_node = current_node.next
    return str(list)
    
  def addNodeAfter(self, new_value, after_node):
    #if isinstance(after_node, int): exec "after_node = self.Node%i" %after_node
    pass  
      
ll = LinkedList(1)
print ll # 1
ll.addNode(2)
print ll #12
ll.addNode(5) 
print ll # 123
ll.addNode(4) #123
print ll
ll.addNode(74)
print ll
ll.removeNode(5)
print ll
#print ll.Node3
