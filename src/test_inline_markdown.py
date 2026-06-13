import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode(
            "this is a test string with `code snippet` in it",
            TextType.TEXT
        )
        test_case = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(test_case[0].text, "this is a test string with ")
        self.assertEqual(test_case[1].text, "code snippet")
        self.assertEqual(test_case[2].text, " in it")

    def test_bold_delimiter(self):
        node = TextNode(
            "this is a test string with **bold words** in it",
            TextType.TEXT
        )
        test_case = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(test_case[0].text, "this is a test string with ")
        self.assertEqual(test_case[1].text, "bold words")
        self.assertEqual(test_case[2].text, " in it")

    def test_italic_delimiter(self):
        node = TextNode(
            "this is a test string with _italic words_ in it",
            TextType.TEXT
        )
        test_case = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(test_case[0].text, "this is a test string with ")
        self.assertEqual(test_case[1].text, "italic words")
        self.assertEqual(test_case[2].text, " in it")
    
    def test_non_text_node(self):
        node = TextNode(
            "_this is a test string with italic words in it_",
            TextType.ITALIC
        )
        test_case = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(test_case[0], node)

    def test_invalid_markdown(self):
        node = TextNode(
            "this is a test string with **bold words in it",
            TextType.TEXT
        )
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_starts_with_delimiter(self):
        node = TextNode(
            "_this is a test string with italic words in it_",
            TextType.TEXT
        )
        test_case = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(test_case[0].text, "this is a test string with italic words in it")
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)