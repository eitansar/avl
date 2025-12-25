# id1:
# name1:
# username1:
# id2:
# name2:
# username2:

import math

from statsmodels.sandbox.regression.try_treewalker import tree2

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.bf = 0

    def __eq__(self,other):
        return self.key == other.key
    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def __repr__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'

    def in_order(self,res):
        if self is None:
            return
        self.left.in_order(res)
        res.append(self.key,self.value)
        self.right.in_order(res)


def is_real_node(self):
    return self is not None




"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self, root=None, max=None):
        self.root = root
        self.max = max

    def __repr__(self):  # you don't need to understand the implementation of this method
        def printree(root):
            if not root:
                return ["#"]

            root_key = str(root.key)
            left, right = printree(root.left), printree(root.right)

            lwid = len(left[-1])
            rwid = len(right[-1])
            rootwid = len(root_key)

            result = [(lwid + 1) * " " + root_key + (rwid + 1) * " "]

            ls = len(left[0].rstrip())
            rs = len(right[0]) - len(right[0].lstrip())
            result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

            for i in range(max(len(left), len(right))):
                row = ""
                if i < len(left):
                    row += left[i]
                else:
                    row += lwid * " "
                row += (rootwid + 2) * " "

                if i < len(right):
                    row += right[i]
                else:
                    row += rwid * " "
                result.append(row)
            return result

        return '\n'.join(printree(self.root))


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
        if r is None:
            return (None,1)
        while r is not None and r.key != key:
            if r.key < key:
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
        if not is_real_node(self.max):
            return (None, 0)
        r = self.max
        counter = 0
        while r.parent.key >= key:
            r = r.parent
            counter += 1
        while r.key != key:
            if not is_real_node(r):
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

    def right_rotation(self,b):
        if b.parent is None:
            x = 'root'
        elif b.parent.left is b:
            x = 'left'
        else:
            x = 'right'
        a = b.left
        if x=='root':
            self.root = a
            a.parent = None
        a_l = height_2(a.left)
        a_r = height_2(a.right)
        b_r = height_2(b.right)
        b.height = max(a_r, b_r) + 1
        a.height = max(b.height, a_l) + 1
        b.left = a.right
        if b.left is not None:
            b.left.parent = b
        a.right = b
        a.parent = b.parent
        if x == 'left':
            a.parent.left = a
        if x == 'right':
            a.parent.right = a
        b.parent = a
        a.bf = height_2(a.left) - height_2(a.right)
        b.bf = height_2(b.left) - height_2(b.right)
    def leftrotation(self,r):
        l = r.right
        if r == self.root:
            self.root = l
        else:
            if r.parent.right == r:
                r.parent.right = l
            else:
                r.parent.left = l
        r.right  =l.left
        l.left = r
        l.parent = r.parent
        r.parent = l
        if r.right is not None:
            r.right.parent = r
        r.height = 1 + max(height_2(r.left), height_2(r.right))
        r.bf = height_2(r.left) - height_2(r.right)

        l.height = 1 + max(height_2(l.left), height_2(l.right))
        l.bf = height_2(l.left) - height_2(l.right)

        return 1
    def insert(self, key, val):
        r = self.root
        if not is_real_node(r):
            root = AVLNode(key, val)
            self.root = root
            root.height = 0
            return (root, 0, 0)
        r_p = None
        counter = 0
        while is_real_node(r):
            if r.key > key:
                r_p = r
                r = r.left
                counter += 1
            else:
                r_p = r
                r = r.right
                counter += 1
        x = AVLNode(key, val)
        if key < r_p.key:
            r_p.left = x

        else:
            r_p.right = x
        x.parent = r_p
        x.height = 0
        x.bf = 0
        h = 0
        while r_p is not None:
            change = (r_p.height != max(height_2(r_p.left), height_2(r_p.right)) + 1)
            r_p.height = max(height_2(r_p.left), height_2(r_p.right)) + 1
            r_p.bf = height_2(r_p.left) - height_2(r_p.right)
            if not change:
                break
            h+=1
            if -2 < r_p.bf < 2:
                r_p = r_p.parent
            else:

                if r_p.bf == -2 and r_p.right.bf== -1:
                    self.leftrotation(r_p)
                elif r_p.bf == -2 and r_p.right.bf == 1:
                    self.right_rotation(r_p.right)
                    self.leftrotation(r_p)

                elif r_p.bf == 2 and r_p.left.bf == -1:
                    self.leftrotation(r_p.left)
                    self.right_rotation(r_p)
                elif r_p.bf == 2 and r_p.left.bf == 1:
                    self.right_rotation(r_p)
        return (x,counter,h)


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
        if node is None:
            return
        if node.right is None and node.left is None:
            if node == self.root:
                self.root = None
                return
            elif node.parent.right == node:
                node.parent.right = None
            elif node.parent.left == node:
                node.parent.left = None
            node = node.parent
        elif node.right is None:
            if node == self.root:
                self.root = node.left
                return
            elif node.parent.right == node:
                node.parent.right = node.left
            elif node.parent.left == node:
                node.parent.left = node.left
            node.left.parent = node.parent
            node = node.parent
        elif node.left is None:
            if node == self.root:
                self.root = node.right
                return
            elif node.parent.right == node:
                node.parent.right = node.right
            elif node.parent.left == node:
                node.parent.left = node.right
            node.right.parent = node.parent
            node = node.parent
        else:
            nodego = node
            nodego = nodego.right
            while nodego.left is not None:
                nodego = nodego.left
            nodepar = nodego.parent
            print(nodepar)
            print(nodego.key)
            if nodepar.right is not None and nodepar.right == nodego:
                nodepar.right = nodego.right
                if nodego.right is not None:
                    nodego.right.parent = nodepar
            if nodepar.left is not None and nodepar.left == nodego:
                nodepar.left = nodego.right
                if nodego.right is not None:
                    nodego.right.parent = nodepar
            node.key = nodego.key
            node.value = nodego.value
        heightchange =0
        if node.height == max(height_2(node.right),height_2(node.left)) +1:
            heightchange =1
        node.bf = height_2(node.left) -height_2(node.right)
        while node is not None and ((node.bf >=2 or node.bf <=-2) or heightchange == 0) :
            if node.bf == -2:
                if node.right.bf == 1:
                    self.right_rotation(node.right)
                    self.leftrotation(node)
                elif node.right.bf == 0:
                    self.leftrotation(node)
                elif node.right.bf == -1:
                    self.leftrotation(node)
            if node.bf == 2:
                if node.left.bf == 1:
                    self.right_rotation(node)
                elif node.left.bf == 0:
                    self.right_rotation(node)
                elif node.left.bf == -1:
                    self.leftrotation(node.left)
                    self.right_rotation(node)
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

    @staticmethod
    def detach_tree(node):
        avl = AVLTree(root=node)
        node.parent = None
        return avl

    def split(self, node):
        smaller = AVLTree.detach_tree(node.left)
        greater = AVLTree.detach_tree(node.right)
        while node.parent is not None:
            n_p = node.parent
            if node is n_p.right:
                smaller.join(AVLTree.detach_tree(n_p.left),n_p.key,n_p.value)
            else:
                greater.join(AVLTree.detach_tree(n_p.right), n_p.key, n_p.value)
            node = n_p

        return smaller,greater

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        res = []
        self.root.in_order(res)
        return res


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




def height_2(node):
    if type(node) == AVLNode:
        return node.height
    else:
        return -1

t = AVLTree()
t.insert(4,2)
t.insert(2,0)
t.insert(1,0)
t.insert(12,1)
t.insert(13,1)


print(t)