class Node:
    instances = []
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.__class__.instances.append(self)
n = Node(50)
n.left = Node(30)
n.right = Node(70)
n.left.left = Node(20)
n.left.right = Node(40)
n.right.left = Node(60)
n.right.right = Node(80)
for instance in Node.instances:
    print(instance.data)
print(n.right.right.data)