from textnode import TextNode, TextType
import re

def split_nodes_delimiter(
        old_nodes: list[TextNode],
        delimiter: str,
        text_type: TextType
    ) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_old_node = old_node.text.split(delimiter)
        if len(split_old_node) % 2 == 0:
            raise Exception("Invalid Markdown syntax")
        for i in range(len(split_old_node)):
            if not split_old_node[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_old_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_old_node[i], text_type))
    return new_nodes

def extract_markdown_images(text: str) -> list[tuple(str, str)]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text: str) -> list[tuple(str, str)]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)