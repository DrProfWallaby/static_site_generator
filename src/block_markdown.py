from enum import Enum
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip() != ""]

def block_to_block_type(block: str) -> BlockType:
    headers = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(headers):
        return BlockType.HEADING
    elif block.startswith("```"):
        split_block = block.split("\n")
        if len(split_block) < 2:
            return BlockType.PARAGRAPH
        if split_block[0] == "```" and split_block[-1] == "```":
            return BlockType.CODE
        return BlockType.PARAGRAPH
    elif block.startswith(">") or block.startswith("> "):
        split_block = block.split("\n")
        for line in split_block:
            if line.startswith(">") or line.startswith("> "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("- "):
        split_block = block.split("\n")
        for line in split_block:
            if line.startswith("- "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif block.startswith("1. "):
        split_block = block.split("\n")
        for i in range(len(split_block)):
            if split_block[i].startswith(f"{i + 1}. "):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> HTMLNode:
    nodes = []
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            count = 0
            for char in block:
                if char == "#":
                    count += 1
                if char != "#":
                    break
            clean_block = block[count + 1:]
            nodes.append(ParentNode(f"h{count}", text_to_children(clean_block)))

        elif block_type == BlockType.PARAGRAPH:
            paragraph = " ".join(block.split("\n"))
            nodes.append(ParentNode("p", text_to_children(paragraph)))

        elif block_type == BlockType.QUOTE:
            quote_lines = block.split("\n")
            clean_lines = []
            for line in quote_lines:
                clean_lines.append(line.lstrip(">").strip())
            nodes.append(ParentNode("blockquote", text_to_children(" ".join(clean_lines))))

        elif block_type == BlockType.UNORDERED_LIST:
            list_lines = block.split("\n")
            li_nodes = []
            for line in list_lines:
                li_nodes.append(ParentNode("li", text_to_children(line[2:])))
            nodes.append(ParentNode("ul", li_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            list_lines = block.split("\n")
            li_nodes = []
            for line in list_lines:
                split_line = line.split(". ", 1)
                li_nodes.append(ParentNode("li", text_to_children(split_line[1])))
            nodes.append(ParentNode("ol", li_nodes))
        
        elif block_type == BlockType.CODE:
            split_block = block.split("```")
            nodes.append(ParentNode("pre", [text_node_to_html_node(TextNode(split_block[1].lstrip("\n"), TextType.CODE))]))
        
    return ParentNode("div", nodes)

def text_to_children(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes