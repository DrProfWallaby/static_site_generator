import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

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
        
    def test_heading(self):
        heading = "# this is a heading"
        block_type = block_to_block_type(heading)
        self.assertEqual(block_type, BlockType.HEADING)

        heading = "## this is a heading"
        block_type = block_to_block_type(heading)
        self.assertEqual(block_type, BlockType.HEADING)

        heading = "### this is a heading"
        block_type = block_to_block_type(heading)
        self.assertEqual(block_type, BlockType.HEADING)

        heading = "#### this is a heading"
        block_type = block_to_block_type(heading)
        self.assertEqual(block_type, BlockType.HEADING)

        heading = "##### this is a heading"
        block_type = block_to_block_type(heading)
        self.assertEqual(block_type, BlockType.HEADING)

        heading = "###### this is a heading"
        block_type = block_to_block_type(heading)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        code = """```
this is a code block
```"""
        block_type = block_to_block_type(code)
        self.assertEqual(block_type, BlockType.CODE)
    
    def test_block_to_block_type_quote(self):
        quote = """>this is a quote line
> so is this
>and this"""
        block_type = block_to_block_type(quote)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_unordered_list(self):
        unordered_list = """- this is a list item
- this is another list item
- and one final list item"""
        block_type = block_to_block_type(unordered_list)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        ordered_list = """1. this is the first item
2. this is the second item
3. this is the fourth item"""
        block_type = block_to_block_type(ordered_list)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_wrong_ordered_list(self):
        ordered_list = """1. this is the first item
3. this is the second item
4. this is the last item"""
        block_type = block_to_block_type(ordered_list)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )