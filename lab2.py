# Author: Elijah Paulman

class Node:
    # Initializes a node with a root and no children
    def __init__(self, key):
        self.key = key  
        self.left = None  
        self.right = None  

class BinarySearchTree:
    # Binary Search Tree class
    def __init__(self):
        # Initializes empty tree
        self.root = None  

    def insert(self, key):
        # If tree is empty, create root node
        if self.root is None:
            self.root = Node(key)  
        else:
            # If tree is not empty, use recursive insert method
            self.insertNotRoot(self.root, key) 

    def insertNotRoot(self, node, key):
        if key < node.key:
            # If key is less than current node's key, go left
            if node.left is None:
                # If left child doesn't exist, insert here
                node.left = Node(key) 
            else:
                # If left child exists, recursive call
                self.insertNotRoot(node.left, key)  
        elif key > node.key:
            # If key is greater than current node's key, go right
            if node.right is None:
                # If right child doesn't exist, insert here
                node.right = Node(key) 
            else:
                # If right child exists, recursive call
                self.insertNotRoot(node.right, key) 

    def search(self, key):
        # Searches starting with root
        return self.searchNotRoot(self.root, key)  

    def searchNotRoot(self, node, key):
        # If node doesn't exist or node is the target, return the node
        if node is None or node.key == key:
            return node  
        if key < node.key:
            # If key is less than current node's key, go left
            return self.searchNotRoot(node.left, key) 
        # If key is greater than current node's key, go right
        return self.searchNotRoot(node.right, key)  

    def delete(self, key):
        # Deletes starting with root
        self.root = self.deleteNotRoot(self.root, key)  
    
    def deleteNotRoot(self, node, key):
        # If node doesn't exist, nothing to delete, return the node
        if node is None:
            return node 
        if key < node.key:
            # If key is less than current node's key, go left
            node.left = self.deleteNotRoot(node.left, key)  
        elif key > node.key:
            # If key is greater than current node's key, go right
            node.right = self.deleteNotRoot(node.right, key) 
        else:
            # If current node is the target
            if node.left is None:
                # If no left child, replace current node with right child
                return node.right 
            elif node.right is None:
                # If no right child, replace current node with left child
                return node.left 
            else:
                # If both children exist
                successor = self.getSuccessor(node.right) 
                # Replace current node's key with successor's key
                node.key = successor.key 
                # Delete successor
                node.right = self.deleteNotRoot(node.right, successor.key) 
        return node 

    def getSuccessor(self, node):
        current = node
        # The successor is the leftmost node
        while current.left is not None:
            current = current.left 
        return current

    def in_order_traversal(self, node):
        # In order traversal method
        result = []
        if node:
            result = self.in_order_traversal(node.left)
            result.append(node.key)
            result = result + self.in_order_traversal(node.right)
        return result

import unittest
from lab2 import BinarySearchTree, Node

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        # Create a binary search tree
        self.bst = BinarySearchTree()  

    def test_insert(self):
        self.bst.insert(5)
        self.bst.insert(3)
        self.bst.insert(7)
        # Make sure root and children are inserted correctly (5 is root, 3 is left child, 7 is right child)
        self.assertEqual(self.bst.root.key, 5)  
        self.assertEqual(self.bst.root.left.key, 3)  
        self.assertEqual(self.bst.root.right.key, 7) 

    def test_search(self):
        self.bst.insert(5)  
        self.bst.insert(3)
        self.bst.insert(7)
        # Search for existing key (5) and non-existing key (10)
        self.assertIsNotNone(self.bst.search(5))  
        self.assertIsNone(self.bst.search(10)) 

    def test_delete(self):
        self.bst.insert(5)  
        self.bst.insert(3)
        self.bst.insert(7)
        # Delete 3 and make sure it is no longer present
        self.bst.delete(3)  
        self.assertIsNone(self.bst.search(3))  

    def test_duplicate_insert(self):
        self.bst.insert(5)
        self.bst.insert(5)        
        self.bst.insert(5)
        # Make sure root equals 5 and no children
        self.assertEqual(self.bst.root.key, 5)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)

    def test_large_input(self):
        for i in range(500):
            self.bst.insert(i)
        # Test large input of 500 nodes
        self.assertEqual(self.bst.search(499).key, 499)  # Change 500 to 499

    def test_in_order_traversal(self):
        for i in [5, 3, 7, 2, 4, 6, 8]:
            self.bst.insert(i)
        # Make sure in order traversal returns the correct order
        self.assertEqual(self.bst.in_order_traversal(self.bst.root), [2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()