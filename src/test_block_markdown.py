import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

    def test_leading_spaces(self):
        md = """
                    This has a lot of leading whitespace at the beginning

Meanwhile, this is just a normal paragraph.
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This has a lot of leading whitespace at the beginning",
                "Meanwhile, this is just a normal paragraph."
            ],
        )

    def test_excessive_newlines(self):
        md = """
This is a paragraph.



This is a paragraph thats further than anticipated.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph.",
                "This is a paragraph thats further than anticipated."
            ]
        )
        