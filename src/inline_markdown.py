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

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for image in images:
            sections = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
            before = sections[0]
            remaining_text = sections[1]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for link in links:
            sections = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
            before = sections[0]
            remaining_text = sections[1]
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes