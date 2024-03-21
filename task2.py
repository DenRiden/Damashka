class Node:
   def __init__(self, data):
       self.data = data
       self.nref = None
       self.pref = None

class Queue:
   def __init__(self):
       self.start = None
       self.end = None

   def pop(self):
       if self.start is None:
           return None
       val = self.start.data
       if self.start.nref:  
           self.start.nref.pref = None
           self.start = self.start.nref
       else:
           self.start = None
           self.end = None
       return val

   def push(self, val):
       new_node = Node(val)
       if self.start is None:
           self.start = new_node
       else:
           new_node.pref = self.end
           self.end.nref = new_node
       self.end = new_node

   def insert(self, n, val):
       new_node = Node(val)
       if n == 0:
           new_node.nref = self.start
           self.start.pref = new_node
           self.start = new_node
       else:
           current = self.start
           for i in range(n - 1):
               if current is None:
                   return
               current = current.nref
           if current is None:
               return
           new_node.nref = current.nref
           new_node.pref = current
           if current.nref is None:
               self.end = new_node
           else:
               current.nref.pref = new_node
           current.nref = new_node

   def print_queue(self):
       current = self.start
       while current:
           print(current.data)
           current = current.nref
