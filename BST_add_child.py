class Node(object):  
     def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here."""

        
        if new_data >= self.data:

            if self.right is None:
                self.right = Node(new_data)
            
            else:
                self.right.insert(new_data)

        else:

            if self.left is None:
                self.left = Node(new_data)

            else:
                self.left.insert(new_data)
