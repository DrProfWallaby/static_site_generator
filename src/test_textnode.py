import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.LINK, "http://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_none(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()