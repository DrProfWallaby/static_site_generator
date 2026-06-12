import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "This is a test HTMLNode", props={"href": "https://www.google.com"})
        node2 = HTMLNode("<p>", "This is a test HTMLNode", props={"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("<p>", "This is a test HTMLNode", props={"href": "https://www.google.com"})
        node2 = HTMLNode("<p>", "This is also a test HTMLNode", props={"href": "https://www.bing.com"})
        self.assertNotEqual(node, node2)

    def test_not_none(self):
        node = HTMLNode("<p>", "This is a test HTMLNode", props={"href": "https://www.google.com"})
        self.assertIsNotNone(node.tag)
        self.assertIsNotNone(node.value)
        self.assertIsNotNone(node.props)