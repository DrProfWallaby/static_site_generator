import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_many_children(self):
        child_node0 = LeafNode("p", "child0")
        child_node1 = LeafNode("b", "child1")
        child_node2 = LeafNode("i", "child2")
        parent_node = ParentNode("div", [child_node0, child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><p>child0</p><b>child1</b><i>child2</i></div>")

    def test_to_html_no_tag(self):
        child0 = LeafNode("p", "i shouldnt see this")
        parent_node = ParentNode(None, children=[child0])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()