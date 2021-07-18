# Here is an example of a binary search tree:

class BST:
    # This defines what the BST will be. Notice that we delclare the Node class (ie what nodes are) below

    class Node:
        # Each node will have data and pointers to each subtree

         def __init__(self, data):
           # Initialize node and provide data for it
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        # Initialize an empty BST
        self.root = None
    
    """
    Inserting Data Example
    """
    def insert(self, data):
        """
        This function will insert data into the BST. If the BST is 
        empty then the self.root will be equal to the new node. If 
        there is data there, then use recursion to find where to place
        the new node and data.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root  

    """
    Notice the difference in names between theses 2 functions
    """
    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if node != None:    
            if data != node.data:
                if data < node.data:
                    # The data belongs on the left side.
                    if node.left is None:
                        # We found an empty spot
                        node.left = BST.Node(data)
                    else:
                        # Need to keep looking.  Call _insert
                        # recursively on the left sub-tree.
                        self._insert(data, node.left)
                else:
                    # The data belongs on the right side.
                    if node.right is None:
                        # We found an empty spot
                        node.right = BST.Node(data)
                    else:
                        # Need to keep looking.  Call _insert
                        # recursively on the right sub-tree.
                        self._insert(data, node.right)

    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
    
    """
    Getting Tree Height
    """

    def get_height(self):
        """

        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    """
    This next function gets the height of the BST by adding 1 (the root)
    and the bigger of the left and right subtrees.
    """
    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0
        else:
            right = self._get_height(node.right)
            left = self._get_height(node.left)
            return 1 + max([left, right])


    
    def __contains__(self, data):
        """
        This function will check to see if the provided data is in the BST.
        It will print a statement if the data is in the BST. 
        """       
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if node != None:
            if data == node.data:
                # print(node.data)
                return True
            elif node.data < data:
                if node.right == None:
                        return False
                else:
                    return self._contains(data, node.right)
            else:
                if node.left == None:
                    return False
                else:
                    return  self._contains(data, node.left)
                    
        

# Test insert function
print("\n Testing Insertion: \n")
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)
for x in tree:
    print(x)  # 1, 3, 4, 5, 6, 7, 10

# Test get height function
print("\n Testing Insertion: \n")
print(tree.get_height()) # 3
tree.insert(6)
print(tree.get_height()) # 3
tree.insert(12)
print(tree.get_height()) # 4

# Test search function