import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("<p>", "This is a test LeafNode", props={"href": "https://www.google.com"})
        node2 = LeafNode("<p>", "This is a test LeafNode", props={"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = LeafNode("<p>", "This is a test LeafNode", props={"href": "https://www.google.com"})
        node2 = LeafNode("<p>", "This is also a test LeafNode", props={"href": "https://www.bing.com"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")