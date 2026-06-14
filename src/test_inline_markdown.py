import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link
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

    def test_split_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
        )
    
    def test_starting_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) That was an image at the beginning of the string.",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
        [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" That was an image at the beginning of the string.", TextType.TEXT)
        ],
        new_nodes
        )

    def test_ending_image(self):
        node = TextNode(
            "There's an image at the end of this string. ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("There's an image at the end of this string. ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes
        )
    
    def test_image_only(self):
        node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes
        )

    def test_image_in_split_nodes_link(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(node, new_nodes[0])