from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str]=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Error: ParentNode has no tag.")
        if not self.children:
            raise ValueError("Error: ParentNode is not a parent.")
        html_string = ""
        for leaf_node in self.children:
            html_string += leaf_node.to_html()
        return f"<{self.tag}>{html_string}</{self.tag}>"
