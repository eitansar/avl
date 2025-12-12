# id1:
# name1:
# username1:
# id2:
# name2:
# username2:


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.bf = 0

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        return self is not None


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def _init_(self):
        self.root = None
        self.max = None

    """searches for a node in the dictionary corresponding to the key (starting at the root)

    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def search(self, key):
        r = self.root
        counter = 1
        while r.key != key:
            if not r.is_real_node():
                return (None, counter)
            if r.key > key:
                r = r.right
                counter += 1
            else:
                r = r.left
                counter += 1
        return (r, counter)

    """searches for a node in the dictionary corresponding to the key, starting at the max

    @type key: int
    @param key: a key to be searched
    @rtype: (AVLNode,int)
    @returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
    and e is the number of edges on the path between the starting node and ending node+1.
    """

    def finger_search(self, key):
        if not self.max.is_real_node():
            return (None, 0)
        r = self.max
        counter = 0
        while r.parant.Key >= key:
            r = r.parent
            counter += 1
        while r.key != key:
            if not r.is_real_node():
                return (None, counter)
            if r.key > key:
                r = r.right
                counter += 1
            else:
                r = r.left
                counter += 1
        return (r, counter)

    """inserts a new node into the dictionary with corresponding key and value (starting at the root)

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    """

    def insert(self, key, val):
        r = self.root
        if not r.is_real_node():
            root = AVLNode(key, val)
            self.root = root
            return (root, 0, 0)
        r_p = None
        counter = 0
        while r.is_real_node():
            if r.key > key:
                r_p = r
                r = r.right
                counter += 1
            else:
                r_p = r
                r = r.left
                counter += 1
        x = AVLNode(key, val)
        if key < r_p.key:
            r_p.left = x

        else:
            r_p.right = x
        x.parant = r_p
        x.height = 0
        self.bf = 0
        h = 0
        while r_p != None:
            change = (r_p.height == max(r_p.left.height, r_p.right.height) + 1)
            r_p.bf = r_p.keft.height - r_p.right.height
            if -2 < r_p.bf < 2 and not change:
                break
            h+=1
            if -2 < r_p.bf < 2:
                r_p = r_p.parent
            else:
                caserotation = 1 if r_p.bf == -2 and r_p.right == -1
                caserotation = 2 if r_p.bf == -2 and r_p.right == 1
                caserotation = 3 if r_p.bf == 2 and r_p.left == -1
                caserotation = 4 if r_p.bf == 2 and r_p.left == 1
                if caserotation == 1:

        return {r, counter}

    """inserts a new node into the dictionary with corresponding key and value, starting at the max

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: (AVLNode,int,int)
    @returns: a 3-tuple (x,e,h) where x is the new node,
    e is the number of edges on the path between the starting node and new node before rebalancing,
    and h is the number of PROMOTE cases during the AVL rebalancing
    """

    def finger_insert(self, key, val):
        return None, -1, -1

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    """

    def delete(self, node):
        return

    """joins self with item and another AVLTree

    @type tree2: AVLTree 
    @param tree2: a dictionary to be joined with self
    @type key: int 
    @param key: the key separting self and tree2
    @type val: string
    @param val: the value corresponding to key
    @pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
    or the opposite way
    """

    def join(self, tree2, key, val):
        return

    """splits the dictionary at a given node

    @type node: AVLNode
    @pre: node is in self
    @param node: the node in the dictionary to be used for the split
    @rtype: (AVLTree, AVLTree)
    @returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
    dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
    dictionary larger than node.key.
    """

    def split(self, node):
        return None, None

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        return None

    """returns the node with the maximal key in the dictionary

    @rtype: AVLNode
    @returns: the maximal node, None if the dictionary is empty
    """

    def max_node(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return -1

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root


def right_rotation(B):
    B.right