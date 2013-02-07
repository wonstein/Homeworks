class Node(object):
  def __init__(self, _value = None, _next = ''):
    self.value = _value
    self.next = _next
  
  def __str__(self):
    return str(self.value)
    
  def getValue(self):
    return self.value
    
  def changeNext(self, new_next):
    self.next = new_next
  
  def getNext(self):
    return self.next
    
class LinkedList(object):
  def __init__(self, value):
    self.tail = Node(None, None)
    self.head = Node(value)
    self.length = 1

  def length(self):
    return length
    
  def addNode(self, new_value):
    if self.length == 1:
      self.tail = Node(new_value)
      self.head.changeNext(self.tail)
    else:
      current_node = self.head
      for i in range(1, self.length):
        current_node = current_node.getNext()
      current_node.changeNext(Node(new_value))
    self.length += 1
    
  def __str__(self):
    current = self.head
    list = []
    for i in range(self.length):
      list.append(current.getValue())
      current = current.getNext()
    return str(list)
      
ll = LinkedList(1)
print ll # 1
ll.addNode(2)
print ll #12
ll.addNode(5) 
print ll # 123
ll.addNode(4) #123
print ll
